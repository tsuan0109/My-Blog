from django import forms
from captcha.fields import CaptchaField

class BoardForm(forms.Form):
    boardsubject = forms.CharField(max_length=100,initial='')
    boardname = forms.CharField(max_length=20,initial='')
    boardmail = forms.EmailField(max_length=100,initial='',required=False)
    boardcontent = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
    
    
class PostForm(forms.Form):
    posttitle = forms.CharField(max_length=100,initial='')
    postcontent = forms.CharField(widget=forms.Textarea(
                       attrs={'rows': 20,
                              'cols': 50}))
    
    
