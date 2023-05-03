from django.shortcuts import render
# from django.http import HttpResponse

# FOR LOGIN & LOGOUT
from django.contrib.auth.views import LoginView, LogoutView
# FOR SIGN UP
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    # return HttpResponse('This is my HOME page...')
    data = {
        'name': 'IBRAHIM ASSOCIATES',
        'contact': '+92 333 666 3896',
        'address': 'Al-Hussain Arched Office # 5 Sector G Bahria Enclave Islamabad'
    }
    return render(request, 'home/home.html', { 'data' : data})


def login(request):
    return render(request, 'home/login.html')


# START SIGN UP
def signup(request):
    return render(request, 'home/signup.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/home'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(self, request, *args, **kwargs)
# END SIGN UP

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = '/post/all'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    # success_url = '/home'
