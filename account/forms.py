from django import forms
from django.contrib.auth.models import User
from .models import *
#Создание формы для регистрации
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password_confirm']

#Создание формы для входа
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
#Создание формы для редактирования
class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name' , 'email')

#Создание формы для редактирования
class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']