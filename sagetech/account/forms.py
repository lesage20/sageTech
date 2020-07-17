from django.forms import ModelForm
from .models import Profile
from website.models import NewsLetter, Contact
from blog.models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        


        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
            
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
    
    def clean_username(self):
        # Get the email
        
        username = self.cleaned_data.get('username')


        # Check to see if any users already exist with this email as a username.
        try:
            
            match = User.objects.get(username=username)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return username

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This username  is already in use. Try another')
        
class NewsletterForm(forms.Form, ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
    
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = NewsLetter.objects.get(email=email)
        except NewsLetter.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class CommentForm(ModelForm):
    message = forms.Textarea(attrs={
        'id': 'comment',
        'name': 'comment'
    })
    class Meta:
        model = Comment
        fields = ['message', ]


    