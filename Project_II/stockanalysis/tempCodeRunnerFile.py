def main_view(request):
    df=yf.download('AAPL',start = '2015-01-01',end = '2022-12-31')
    print(df)
    return render(request,'graph.html',{})