from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', main),
    path('post/<int:postid>/', post),
    path('postCreate/', PostCreate),
    path('messages/', Mess),
    path('login/',
         LoginView.as_view(template_name='flatpages/Account123/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='flatpages/Account123/logout.html'),
         name='logout'),
    path('registretion/',
         BaseRegisterView.as_view(template_name='flatpages/Account123/registretion.html'),
         name='registretion'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


