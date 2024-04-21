from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Urlshortner
from django.views import View
from django.conf import settings


from .serializers import LinkSerializer 

# Create your views here.


class ShortnerListApiView(ListAPIView):
    queryset = Urlshortner.objects.all()
    serializer_class = LinkSerializer

class ShortnerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer
    
class RedirectLink(View):
    def get(self, request, short_url, *args, **kwargs):
        shortened_url = settings.HOST_URL+'/'+self.kwargs['short_url']
        redirect_link = Urlshortner.objects.filter(short_url=shortened_url).first().original_url
        if redirect_link:
            return redirect(redirect_link)
        else:
            return redirect('/404/')


def index(request):
    return render(request, 'base.html')
