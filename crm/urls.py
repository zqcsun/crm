from django.urls import path
from . import views

app_name =  'crm'

urlpatterns = [
    path('', views.LeadsViews.as_view(), name='lead_url'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail_url'),
    path('create/', views.LeadCreateView.as_view(), name='lead_create_url'),
    path('update/<int:pk>/', views.LeadUpdateView.as_view(), name='lead_update_url'),
    path('delete/<int:pk>/', views.LeadDeleteView.as_view(), name='lead_delete_url'),
    path('managers/', views.ManagersViews.as_view(), name='manager_url'),
]