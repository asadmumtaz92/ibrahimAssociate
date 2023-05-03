from django.contrib import admin
from django.urls import path, include
from home.urls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', views.home, name='home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('post/', include('myPosts.urls')),
]
