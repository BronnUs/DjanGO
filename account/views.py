from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from basket.models import Order
# Create your views here.

#view страницы профиля
def profile_pg(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile': profile, 'user':user})

#view страницы регистрации
def register(request):
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return redirect(to='/profile/login/')
    else:
        reg_form = RegisterForm()
    return render(request, 'register.html', {'reg_form': reg_form})

#view страницы входа
def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='/shop/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#view страницы выхода
def my_logout(request):
    logout(request)
    return redirect(to='/shop/')

#view страницы редактирования
def profileChange(request):
    if request.method == 'POST':
        user_form = UserEdit(instance=request.user, data=request.POST)
        profile_form = ProfileEdit(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='/profile/{}'.format(request.user.get_username()))
    else:
        user_form = UserEdit(instance=request.user)
        profile_form = ProfileEdit(instance=request.user.profile)
        return render(request,
                      'change.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})