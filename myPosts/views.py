from django.shortcuts import render
# from django.views.generic import ListView, DeleteView, CreateView, UpdateView
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin

from .models import myPosts_1

# VIEW ALL POSTS
def allPost(request):
    data = myPosts_1.objects.all()
    return render(request, 'myPosts/allPost.html', { 'data': data })


# VIEW POST DETAIL
def postDetail(request):
    return render(request, 'myPosts/detailPost.html')


# UPDATE POST
def postUpdate(request):
    return render(request, 'myPosts/updatePost.html')


# DELETE POST
def deletePost(request):
    return render(request, 'myPosts/deletePost.html')





# PostListView
# PostDetailView
# PostUpdateView
# PostDeleteView

# class PostListView(ListView):
#     # model = Posts
#     # context_object_name = "allPosts"
#     template_name = 'posts/allPosts.html'
#     # login_url = '/login'
