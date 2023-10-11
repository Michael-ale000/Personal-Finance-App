from django.urls import path
from .import views

urlpatterns = [
    path('portfolio/',views.portfolio,name="portfolio"),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
]
