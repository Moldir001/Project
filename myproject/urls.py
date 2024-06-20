from django.conf import settings
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('category/<int:catid>/', show_category, name='show_category'),
    path('price/', price, name='price'),
    path('home/', homepage, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('posts/<int:post_id>/', posts_detail, name='posts_detail'),
    path('posts_sort/', posts_sort, name='posts_sort'),
    path('base/', base, name='base'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', signup, name='signup'),
]

handler404 = pagenotfound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

