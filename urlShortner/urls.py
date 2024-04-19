from django.urls import path
from urlShortner.views import ShortnerCreateApiView, ShortnerListApiView

urlpatterns = [
    path('', ShortnerListApiView.as_view(), name='all_list'),
    path('create/', ShortnerCreateApiView.as_view(), name='create_'),
]