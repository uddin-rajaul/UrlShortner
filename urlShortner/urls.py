from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-url/', views.create_short_url, name='create_short_url'),
    path('edit/<str:short_code>/', views.edit_url, name='edit_url'),
    path('delete/<str:short_code>/', views.delete_url, name='delete_url'),
    
    # API paths
    path('api/list/', views.ShortnerListApiView.as_view(), name='api_list'),
    path('api/create/', views.ShortnerCreateApiView.as_view(), name='api_create'),
]
