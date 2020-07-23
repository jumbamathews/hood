from django import forms
from .models import Profile, Business, Neighborhood, Post, Comment

    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighborhood','name'] 
        


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name','hood_image','location', 'occupants')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighborhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 30, 'rows': 3}),
   }
