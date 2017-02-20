from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse


def login_view(request):

    logout(request)
    if request.POST:
        user_login = request.POST['login']
        password = request.POST['password']

        user = authenticate(username=user_login, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')

    return TemplateResponse(request, 'login.html')


@login_required(login_url='/login/')
def main_view(request):
    return TemplateResponse(request, 'main.html',
                            context={'user': request.user})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
