from django.urls import path
from . import views

urlpatterns = [
    #path('chart/', views.chart_view, name='chart'),
    #path('graph/', views.main_view, name='graph'),
    #path('stockchart/', views.stock_chart, name='stockchart'),
    # path('stockchart/', views.stock_chart_real, name='stockchart'),
    path('filterstocks/', views.filterstocks, name='filterstocks'),
    path('streamlit/', views.streamlit_page, name='streamlit'),
    path('land/',views.landing ,name="landing"),
    #path('analyst_recommendations/', views.stock_analyst_recommendations, name='stock_analyst_recommendations'),
    
]