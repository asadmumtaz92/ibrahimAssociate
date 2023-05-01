from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is my HOME page...')
    data = {
        'name': 'Malick Asad Mumtaz',
        'age': 29,
    }
    return render(request, 'home/home.html', { 'data' : data})

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def logout(request):
    return render(request, 'home/logout.html')
