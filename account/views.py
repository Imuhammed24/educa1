from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import PermissionRequiredMixin


def login_view(request):
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['pass']
        print(request.POST['pass'])
        user = authenticate(username=username, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect('account:home')
                # return HttpResponse('Logged in')
        else:
            return HttpResponse('Disabled Account')
    else:
        return HttpResponse('Invalid Login')


def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # profile = Profile.objects.create(user=new_user)
            return redirect('account:home')
    else:
        user_form = UserRegistrationForm()

    return redirect('account:home')


def account_view(request):
    context = {'page_name': 'account',
               'signup_form': UserRegistrationForm(),
               'html_title': 'HOME'}
    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    # return render(request, 'registration/logged_out.html')
    return redirect('account:home')



# from django.contrib.auth.mixins import PermissionRequiredMixin
#
# class MyView(PermissionRequiredMixin, View):
#     permission_required = 'polls.add_choice'
#     # Or multiple of permissions:
#     permission_required = ('polls.view_choice', 'polls.change_choice')
