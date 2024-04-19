from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from urlShortner.views import RedirectLink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urlShortner.urls')),
    path('<slug:short_url>/', RedirectLink.as_view(), name='redirect_link')
]
