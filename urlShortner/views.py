from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ShortURL
from .serializers import LinkSerializer

# API Views
class ShortnerListApiView(ListAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = LinkSerializer

class ShortnerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer
    
def redirect_to_original(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code)
    url_instance.click_count += 1
    url_instance.save()
    return redirect(url_instance.original_url)

def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('index')

@login_required(login_url='/login/')
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'urls': urls})

@login_required(login_url='/login/')
def create_short_url(request):
    if request.method == "POST":
        original_url = request.POST.get('original_url')
        custom_code = request.POST.get('custom_code')
        
        if original_url:
            if custom_code:
                if ShortURL.objects.filter(short_code=custom_code).exists():
                    return render(request, 'create.html', {'error': 'Custom code already exists'})
                ShortURL.objects.create(user=request.user, original_url=original_url, short_code=custom_code)
            else:
                ShortURL.objects.create(user=request.user, original_url=original_url)
            return redirect('dashboard')
    return render(request, 'create.html')

@login_required(login_url='/login/')
def edit_url(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code, user=request.user)
    if request.method == "POST":
        original_url = request.POST.get('original_url')
        if original_url:
            url_instance.original_url = original_url
            url_instance.save()
            return redirect('dashboard')
    return render(request, 'edit.html', {'url': url_instance})

@login_required(login_url='/login/')
def delete_url(request, short_code):
    url_instance = get_object_or_404(ShortURL, short_code=short_code, user=request.user)
    if request.method == 'POST':
        url_instance.delete()
    return redirect('dashboard')
