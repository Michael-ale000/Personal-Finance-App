import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models  import load_model
import streamlit as st
import yfinance as yf
import datetime


st.title('Stock Trend Prediction')
stock_categories = {
    'Technology': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META'],
    'Financials': ['JPM', 'BAC', 'WFC', 'C', 'GS'],
    'Consumer Staples': ['PG', 'KO', 'PEP', 'MCD', 'CL'],
    'Automotive': ['TSLA', 'F', 'GM', 'HMC', 'TM'],
    'Retail': ['WMT', 'TGT', 'COST', 'AMZN', 'HD'],
    'Pharmaceuticals': ['JNJ', 'PFE', 'MRK', 'ABBV', 'GSK'],
    'Retail (Auto Parts)': ['AAP', 'ORLY', 'AZO', 'CMG', 'DPZ'],
    'Sports and Fitness': ['NKE', 'LULU', 'UA', 'ADDYY', 'SNOW'],
    'Health Insurance': ['UNH', 'CVS', 'ANTM', 'AET', 'CI'],
    'Telecommunications': ['VZ', 'T', 'TMUS', 'CCI', 'SBAC']
}
selected_category = st.selectbox('Select a Category', list(stock_categories.keys()))
user_input = st.selectbox(f'Select a Stock in {selected_category}', stock_categories[selected_category])
current_date = datetime.datetime.now().date()
df=yf.download(user_input,start = '2016-01-01',end = current_date )
###current status###
# Get the most recent data point
current_status = df.iloc[-1]

# Display the current status
st.subheader('Current Stock Status')
st.write(current_status)


#describing data 
st.subheader('Data From 2016 to 2023')
st.write(df.describe())
# Get the most recent data point


#visualization
st.subheader('Closing price VS Time Chart')
fig1=plt.figure(figsize=(12,6))
plt.plot(df.Close)
plt.xlabel('Time')
plt.ylabel('Price')
st.pyplot(fig1)

#plotting 100 days moving average
st.subheader('Closing price VS Time Chart with 100MA')
ma100=df.Close.rolling(100).mean()
fig3=plt.figure(figsize=(12,6))
plt.plot(df.Close,label='Closing Price')
plt.plot(ma100,'Red',label='100days moving average')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig3)


#plotting 200days moving average
st.subheader('Closing VS Time Chart with 100MA & 200MA')
ma200=df.Close.rolling(200).mean()
fig4=plt.figure(figsize=(12,6))
plt.plot(df.Close,label='Original Closing Price')
plt.plot(ma100,'Red',label='100days moving average')
plt.plot(ma200,'Green',label='200days moving average')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig4)

#splitting data into training data which will be 70 % of the whole data 
#testing data will be remaining 30 % of the whole data
data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
data_training_array=scaler.fit_transform(data_training)



#load my model
model=load_model('keras_stock_prediction_model.h5')

#testing part

past_100_days=data_training.tail(100)
final_df=pd.concat([past_100_days,data_testing],ignore_index=True)
input_data=scaler.fit_transform(final_df)
x_test=[]
y_test=[]
for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])
    
x_test,y_test=np.array(x_test),np.array(y_test)
y_predicted=model.predict(x_test)
scaler=scaler.scale_ #for determinit the scale factor through which we have previously scaled it down
scale_factor=1/scaler[0]
y_predicted=y_predicted * scale_factor
y_test=y_test*scale_factor


#final Graph
st.subheader('Prediction vs Original')
fig2=plt.figure(figsize=(12,6))
plt.plot(y_test,'blue',label='Original Price')
plt.plot(y_predicted,'red',label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
