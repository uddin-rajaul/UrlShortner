from django.contrib import admin
from django.urls import path, include
from urlShortner.views import redirect_to_original

from django.http import HttpResponse

def empty_favicon(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', empty_favicon),
    path('', include('urlShortner.urls')),
    path('<str:short_code>/', redirect_to_original, name='redirect'),
]
