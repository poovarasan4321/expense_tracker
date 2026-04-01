from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('add/', views.add_expense),
    path('report/', views.report),
    path('download/', views.download_report),
      # NEW
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]