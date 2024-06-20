from os import stat
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from myapp.models import *
from django.shortcuts import render, get_object_or_404
from .models import Posts, Categories
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserLoginForm, UserSignupForm
from django.conf.urls.static import static





menu = ["Добавить", "О нас", "Логин", "Регистрация"]

def index(request):
    all_posts = Posts.objects.all()
    categ = Categories.objects.all()
    return render(request, 'home.html', {'title': 'Главная страница', 'all': all_posts, 'categ': categ})



def price(request):
    return HttpResponse("34500")

def pagenotfound(request, exception):
    return HttpResponseBadRequest('вы ошиблись')

def about_us(request):
    return render(request, 'about_us.html')

def posts_sort(request):
    foods = {
        'Горячие блюда': Posts.objects.filter(title='Горячие блюда'),
        'Салаты': Posts.objects.filter(title='Салат'),
        'Десерты': Posts.objects.filter(title='Десерты'),
        'Фастфуд': Posts.objects.filter(title='Фастфуд')
    }
    categ = Categories.objects.all()
    return render(request, 'our_food.html', {'foods': foods, 'categ': categ})

# def show_post(request, post_id):
#     post = get_object_or_404(Posts, id=post_id)
#     categ = Categories.objects.all()
#     return render(request, 'our_players.html', {
#         'title': post.title,
#         'post': post,
#         'categ': categ
#     })

def show_category(request, catid):
    posts = Posts.objects.filter(categoria_id=catid)
    categ = Categories.objects.all()
    selected_category = get_object_or_404(Categories, pk=catid)
    return render(request, 'our_food.html', {'posts': posts, 'categ': categ, 'selected': selected_category})


def posts_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def homepage(request):
    username = request.user.username
    posts = Posts.objects.all()
    return render(request, 'home.html', {'username': username, 'posts': posts})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def base(request):
    return render(request, 'base.html')


def user_logout(request):
    logout(request)
    return redirect('login')