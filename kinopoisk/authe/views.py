from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from re import search

from .models import User
from .forms import UserSignInForm, UserSignUpForm

# Create your views here.
class SignIn(View):
    def get(self, request):
        form = UserSignInForm()

        context = {
            'title': 'Авторизация',
            'form': form,
        }

        return render(request, 'authe/signin.html', context=context)
    
    def post(self, request):
        form = UserSignInForm(request, request.POST)
        if len(request.POST['username']) > 0 and len(request.POST['password']) > 0:
        # if form.is_valid():
            try:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                if user:
                    login(request, user)
                    return redirect(reverse_lazy('movies:index'))
                else:
                    context = { 'form': form, 'error': 1 }
                    return render(request, 'authe/signin.html', context=context)
            except:
                context = { 'form': form, 'error': 2 }
                return render(request, 'authe/signin.html', context=context) 
        else:
            context = { 'form': form, 'error': 3 }
            return render(request, 'authe/signin.html', context=context) 
    

class SignUp(View):         # session based
    def get(self, request):
        form = UserSignUpForm()

        context = {
            'title': 'Регистрация',
            'form': form,
        }

        return render(request, 'authe/signup.html', context=context)
    
    def post(self, request):
        form = UserSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            password = data.pop('password')
            password_pattern = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$'
            if search(password_pattern, password):
                user = User.objects.create(
                    image=data['image'],
                    username=data['username'],
                    email=data['email'],
                )
                user.set_password(password)
                user.save()
                return redirect(reverse_lazy('authe:signin'))
            else:
                context = {'form': form, 'error': 1}
                return render(request, 'authe/signup.html', context=context)
        else:
            context = {'form': form, 'error': 2}
            return render(request, 'authe/signup.html', context=context)

   
@method_decorator(login_required, name='get')
class Profile(View):
    def get(self, request):
        context = {
            'user': request.user,
        }

        return render(request, 'authe/profile.html', context=context)
    

def signout(request):
    logout(request)
    return redirect(reverse_lazy('movies:index'))