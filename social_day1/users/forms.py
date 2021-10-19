from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username','email','password1','password2']
        help_text = {'password1':None}
        exclude = ('password1.help_text',)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args,**kwargs)
        self.fields['password1'].help_text=None

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

