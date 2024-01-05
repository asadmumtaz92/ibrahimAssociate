from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect # HttpResponse
from myPosts.form import ImageForm, PostForm
from myPosts.models import Images, Posts
# from django.db.models.query import QuerySet

# from django.views.generic import ListView, DeleteView, CreateView, UpdateView
# from django.views.generic.edit import DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin


# START VIEW ALL POSTS
@login_required(login_url=('/login'))
def allPost(request):
    data = Posts.objects.all()
    data_img = Images.objects.get(pk=1)
    return render(request, 'myPosts/allPost.html', { 'data': data, 'data_img': data_img })
# END VIEW ALL POSTS


# START VIEW POST DETAIL
def postDetail(request, pk):
    data = Posts.objects.get(pk=pk)
    return render(request, 'myPosts/detailPost.html',{'data': data})
# END VIEW POST DETAIL


# UPDATE POST
def postUpdate(request):
    return render(request, 'myPosts/updatePost.html')


# DELETE POST
def deletePost(request):
    return render(request, 'myPosts/deletePost.html')


# CREATE POST
@login_required
def create(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=2)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post_id=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request, "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/post/all/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'myPosts/createPost.html', {'postForm': postForm, 'formset': formset})




# PostListView
# PostDetailView
# PostUpdateView
# PostDeleteView

# class PostListView(ListView):
#     # model = Posts
#     # context_object_name = "allPosts"
#     template_name = 'posts/allPosts.html'
#     # login_url = '/login'
