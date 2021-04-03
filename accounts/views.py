from django.shortcuts import render, HttpResponse, redirect
from .models import ProfileCreation
from .forms import ProfileCreationForm, ProfileDetailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# SIGN UP
def justreg(request):
    if request.method == 'POST':
        form1 = ProfileCreationForm(request.POST)
        form2 = ProfileDetailForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form2_final = form2.save(commit=False)
            form1_final = form1.save(commit=False)

            form2_final.login = form1_final.username
            form2_final.save()
            form1_final.save()
            return redirect('main')
    else:
        form1 = ProfileCreationForm()
        form2 = ProfileDetailForm()

    context = {
        'form1': form1,
        'form2': form2
    }
    return render(request, 'accounts/register1.html', context)


# SIGN IN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('main')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'accounts/login.html', {})


def main(request):
    return render(request, 'accounts/main.html')


@login_required
def user_logout(request):
    logout(request)
