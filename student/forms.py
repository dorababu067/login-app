from django import forms
from django.contrib.auth.models import User
from student.models import studentInfo

class studentForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields = ["username","password"]
       
class studentInfo_form(forms.ModelForm):
     name = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
     age = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
     address = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control"}))

     class Meta:
        model = studentInfo
        fields = ["name","age","address"]