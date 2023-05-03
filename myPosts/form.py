from django import forms
from .models import Posts, Images

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # description = forms.Textarea()
 
    class Meta:
        model = Posts
        fields = ('title', 'description', 'demand', 'type', 'size', 'sector' )
        labels = {
            'title' : 'Enter post title:',
            'description' : 'Enter post description:',
        }
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Post Image:')    
    class Meta:
        model = Images
        fields = ('image',)



# from django import forms
# from .models import Posts_1, Images_1

# class PostForm(forms.ModelForm):
#     title = forms.CharField(max_length=100)
#     description = forms.Textarea()
#     # demand = '500000'
#     # viewed = '0'
 
#     class Meta:
#         model = Posts_1
#         # fields = ('title', 'description', 'demand', 'viewed' )
#         fields = ('title', 'description', )
 
 
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Post Image:')    
#     class Meta:
#         model = Images_1
#         fields = ('image',)



# # from django import forms
# # from .models import Posts, Images

# # class PostForm(forms.ModelForm):
# #     title = forms.CharField(max_length=128)
# #     body = forms.CharField(max_length=245, label="Item Description.")
 
# #     class Meta:
# #         model = Posts
# #         fields = ('title', 'body', )
 
 
# # class ImageForm(forms.ModelForm):
# #     image = forms.ImageField(label='Image')    
# #     class Meta:
# #         model = Images
# #         fields = ('image', )
