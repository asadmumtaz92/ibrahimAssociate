from django.urls import path
from . import views

urlpatterns = [
    # path('all/', views.PostListView.as_view(), name='posts.allPosts'),
    # path('<int:pk>', views.PostDetailView.as_view(), name='posts.postDetail'),
    # path('update/<int:pk>', views.PostUpdateView.as_view(), name='posts.update'),
    # path('update/<int:pk>', views.PostDeleteView.as_view(), name='posts.update'),

    path('all/', views.allPost, name='myPosts.allPost'),
    path('<int:pk>', views.postDetail, name='myPosts.postDetail'),
    path('update/<int:pk>', views.postUpdate, name='myPosts.update'),
    path('delete/<int:pk>', views.deletePost, name='myPosts.delete'),
    path('create/', views.create, name='myPosts.create')
]
