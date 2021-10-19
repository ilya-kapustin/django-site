from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.views.generic import CreateView, UpdateView
from .forms import RegisterForm, UserUpdateForm
from .models import Profile


# class GroupUpdate(UpdateView):
#     model = User
#     form_class = RegisterForm
#     template_name = 'app_users/profile.html'
#     # fields = ['social', 'address']
#     success_url = '/'

@login_required
def profile_edit(request):
    user = request.user
    profile = request.user.profile
    form = UserUpdateForm(request.POST or None, request.FILES,
                          initial={'first_name': user.first_name, 'last_name': user.last_name, 'img': profile.img})
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            profile.img = request.FILES['img']

            user.save()
            profile.save()
            return HttpResponseRedirect('/')

    context = {
        "profile": profile,
        "form": form,
        'title': 'Редактирование профиля',
    }

    return render(request, "app_users/profile.html", context)


class AnotherLogoutView(LogoutView):
    template_name = 'app_users/logout.html'


class LoginUser(LoginView):
    model = User
    template_name = 'app_users/login.html'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            address = form.cleaned_data.get('address')
            brightday = form.cleaned_data.get('brightday')
            social = form.cleaned_data.get('social')
            img = form.cleaned_data.get('img')
            Profile.objects.create(
                user=user,
                address=address,
                brightday=brightday,
                social=social,
                img=img,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/registration.html', {'form': form})
