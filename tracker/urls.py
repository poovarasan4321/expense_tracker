from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add/', views.add_expense),
    path('report/', views.report),
    path('download/', views.download_report),
]