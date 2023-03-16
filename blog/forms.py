from django import forms
from blogapp.models import*


# class USerforms(forms.ModelForm):
#     class Meta:
#         model=Userdata
#         fields='__all__'


class Blogforms(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'        

class Contactform(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'        
