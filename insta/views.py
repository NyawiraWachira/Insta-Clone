from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm



# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account Created Successfully! You are now able to log in")

                return redirect('login')


        return render(request, 'authenticate/register.html',{'form':form} )
      
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

            else:
                messages.info(request, 'Check username or password and try again')

        return render(request, 'authenticate/login.html' )

def logoutUser(request):
    logout(request)

    return redirect('login')

