from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from .forms import ( UserRegistrationForm , UserProfileForm,
                     UserUpdateForm, ProfileLinksForm 
                     )
                        
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.views import LoginView, login_required, logout_then_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, ProfileLinks
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'you are successfully logged in as {username}')
            return redirect('/')

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html' , {'form':form})

def publicProfileView(request, username):
    return HttpResponse("passed")



def profileView(request):
    if request.method == "POST":
        u_instance = User.objects.get(username=request.user.username)
        pl_instance, created = ProfileLinks.objects.get_or_create(user_profile=request.user.userprofile)
        u_form = UserUpdateForm(request.POST, instance=u_instance)
        up_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        pl_form = ProfileLinksForm(request.POST, instance=pl_instance)

        if u_form.is_valid() and up_form.is_valid() and pl_form.is_valid():
            u_form.save()
            pl_form.save()
            up_form.save()

            messages.info(request, "profile updated successfully")
            return redirect(reverse_lazy('accounts:profile'))
    
    else:
        u_instance = User.objects.get(username=request.user.username)
        pl_instance, created = ProfileLinks.objects.get_or_create(user_profile=request.user.userprofile)
        u_form = UserUpdateForm(instance=u_instance)
        up_form = UserProfileForm(instance=request.user.userprofile)
        pl_form = ProfileLinksForm(instance=pl_instance)


        forms = {
            "u_form":u_form,
            "up_form":up_form,
            "pl_form":pl_form
        }
    return render(request, 'accounts/profile.html', forms)


# def userLogin(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             print("form is valid")
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(password)
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('accounts:profile')

#     else:
#         print("sdfjsdfgkjsdgfsdfghsdfv")
#         form=AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form':form})

class userLogin(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

def userLogout(request):
    
    return logout_then_login(request)