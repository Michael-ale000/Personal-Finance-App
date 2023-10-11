# views.py
from django.shortcuts import render
import plotly.graph_objs as go
import yfinance as yf
from .utils import get_plot
import pandas as pd
import plotly.express as px
from .forms import searchform
import subprocess,os
from django.contrib.auth.decorators import login_required



#######################################

########################################################

########################################

# views.py
import plotly.graph_objs as go


@login_required(login_url='index')
def landing(request):
    symbol=None
    if request.method=='POST':
        symbol=request.POST.get('query')
    # Fetch stock data from Yahoo Finance
    stocksymbol=str(symbol)
    df = yf.download(stocksymbol, period="1y", interval="1d")
    
    # Create a Plotly figure
    fig = go.Figure()

    # Add a time vs. closing price trace
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name="AAPL Closing Price"))

    # Customize the chart layout
    fig.update_layout(
        title=" Time vs. Closing Price",
        xaxis_title="Time",
        yaxis_title="Closing Price",
    )

    # Convert the figure to HTML
    plot_div = fig.to_html(full_html=False)
    ###########index graph######
    sp500=yf.Ticker('^GSPC')
    sp500_data=sp500.history(period="1y")
    fig2=go.Figure()
    fig2.add_trace(go.Scatter(x=sp500_data.index, y=sp500_data['Close'], mode='lines', name='S&P 500 Close Price'))
    
    plot_div2 = fig2.to_html(full_html=False)
    sp500_info=sp500.info
    #get the most recent closing price
    current_price=sp500_data['Close'].iloc[-1]
    high_price = sp500_data['High'].iloc[-1]
    low_price = sp500_data['Low'].iloc[-1]
    previous_close = sp500_data['Close'].iloc[-2] # Close price of the previous day
    traded_volume = sp500_data['Volume'].iloc[-1]  # Volume of shares traded today
    percentage_change = ((current_price - previous_close) / previous_close) * 100
    #percentage_change=-2
    fig2.update_layout(
        title='S&P 500 Index Chart',
        xaxis_title='Date',
        yaxis_title='Close Price',
        xaxis=dict(showgrid=False),  # Remove grid lines on the x-axis
        yaxis=dict(showgrid=False),
    )
    if percentage_change<0:
        fig2.update_layout(
            paper_bgcolor='white',  # Change the background color here
            plot_bgcolor='pink',
        )
    else:
        fig2.update_layout(
            paper_bgcolor='white',  # Change the background color here
            plot_bgcolor='lightgreen',
        )
        
    plot_div2 = fig2.to_html(full_html=False)
    context = {"plot_div": plot_div, 
             "stockname":stocksymbol,
             "plot_div2":plot_div2,
             "current_price":current_price,
             "high_price":high_price,
             "low_price":low_price,
             "previous_close":previous_close,
             "traded_volume":traded_volume,
             "percentage_change":percentage_change,
             }
    return render (request, "landingpage.html", context)

#############################################################
#form ###
@login_required(login_url='index')
def filterstocks(request):
    if request.method =='POST':
        form=searchform(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            min_pe_ratio = form.cleaned_data['min_pe_ratio']
            max_pe_ratio = form.cleaned_data['max_pe_ratio']
            sp500_symbols=sp500_stocks = [
                    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB',  # Technology
                    'JPM', 'BAC', 'WFC', 'C', 'GS',  # Financials
                    'PG', 'KO', 'PEP', 'MCD', 'CL',  # Consumer Staples
                    'TSLA', 'F', 'GM', 'HMC', 'TM',  # Automotive
                    'WMT', 'TGT', 'COST', 'AMZN', 'HD',  # Retail
                    'JNJ', 'PFE', 'MRK', 'ABBV', 'GSK',  # Pharmaceuticals
                    'AAP', 'ORLY', 'AZO', 'CMG', 'DPZ',  # Retail (Auto Parts)
                    'NKE', 'LULU', 'UA', 'ADDYY', 'SNOW',  # Sports and Fitness
                    'UNH', 'CVS', 'ANTM', 'AET', 'CI',  # Health Insurance
                    'VZ', 'T', 'TMUS', 'CCI', 'SBAC'  # Telecommunications
    # Add more as needed
                     ]

            filtered_stock=[]
            for symbol in sp500_symbols:
                stock=yf.Ticker(symbol)
                try:
                    stock_info=stock.info
                    pe_ratio = stock_info.get('trailingPE', None)
                    # pb_ratio = stock_info.get('trailingPB', None)
                    price = stock_info.get('regularMarketPreviousClose', None)
                    if (pe_ratio is not None  and price is not None and
                        min_pe_ratio <= pe_ratio <= max_pe_ratio and
                        min_price <= price <= max_price):
                        filtered_stock.append(stock_info)
                        print(price)
                except Exception as e:
                    pass
            return render(request,'screener.html', {'filtered_stock': filtered_stock})
    else:
        form=searchform()
    content={
            'form':form,
        }  
            
    return render(request,'filter_stocks.html',content)
            
            
            
 
 
#################################
@login_required(login_url='index')
def streamlit_page(request):
    return render(request,'streamlit_page.html')    


