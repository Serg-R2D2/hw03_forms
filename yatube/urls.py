"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path


urlpatterns = [
        # раздел администратора
        path('admin/', admin.site.urls),
        # flatpages
        path('about/', include('django.contrib.flatpages.urls')),
        # регистрация и авторизация
        path('auth/', include('users.urls')),
        path('auth/', include('django.contrib.auth.urls'))
        # импорт из приложения posts
]


urlpatterns += [
        path('about-author/', views.flatpage, {'url': '/about-author/'}, name='about'),
        path('about-spec/', views.flatpage, {'url': '/about-spec/'}, name='spec'),
        path('', include('posts.urls'))
]