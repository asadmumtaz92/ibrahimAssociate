from django.contrib import admin
from django.urls import path, include
from home.urls import views

# from myStore.urls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('home/', views.home),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('post/', include('myPosts.urls'), name='post'),
    path('store/', include('myStore.urls'), name='store'),
]
