import re
from django.shortcuts import redirect, render
from .models import Messages
from .forms import MessageForm
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def main_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'main_page.html', {
            'username':username,
            'room_name': 'chat'
        })
    else:
        return render(request, 'main_page.html', {
            'room_name': 'chat'
        })

def get_data(request):
    todo_list = Messages.objects.all()
    ret =[]
    for el in todo_list:
        ret.append({'name':el.name,
                    'message':el.message,
                    })
    return JsonResponse(ret,safe=False)

class MyLoginView(LoginView):
    template_name = 'login.html'