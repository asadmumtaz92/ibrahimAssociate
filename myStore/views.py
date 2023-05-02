from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from myStore.form import ImageForm, PostForm
from myStore.models import Images_1

# @login_required
def postss(request):
    ImageFormSet = modelformset_factory(Images_1, form=ImageForm, extra=2)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images_1.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images_1(post_id=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request, "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images_1.objects.none())
    return render(request, 'myStore/index.html', {'postForm': postForm, 'formset': formset})
