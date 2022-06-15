from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm


# Create your views here.
class Login(LoginRequiredMixin, TemplateView, ):
    template_name = 'flatpages/Account123/login.html'


# Create your views here.


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
    template_name = 'flatpages/Account123/registretion.html'


# Create your views here.

def post(request,postid):
    search_query = request.GET.get('q')

    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all()

    return render(request, 'flatpages/Posts/posts.html', {'posts': posts})


def PostCreate(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        form.save()
        return redirect('/')

    return render(request, 'flatpages/Posts/PostCreate.html', {'form': form})


def Mess(request):
    messages = Mes.objects.all()
    return render(request, 'flatpages/message/html/Messages.html', {'messages': messages})


def main(request):
    return render(request, 'flatpages/main/html/main.html')

