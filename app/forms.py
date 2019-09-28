from django import forms
from django.contrib.auth.models import User
from .models import *
class userform(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','email')

class userprofileform(forms.ModelForm):
    class Meta():
        model = userprofile
        fields = ('phone','sem','usn','branch','eve','college')
        exclude = ['info']
