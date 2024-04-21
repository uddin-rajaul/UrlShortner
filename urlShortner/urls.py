from django.urls import path
from urlShortner.views import ShortnerCreateApiView, ShortnerListApiView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', ShortnerListApiView.as_view(), name='all_list'),
    path('create/', ShortnerCreateApiView.as_view(), name='create_'),
]