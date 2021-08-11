"""neacipeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from neacipe import views
from blog import views as b_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('search/', views.search, name='search'),
    path('result/', b_views.result, name='result'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('<str:id>', b_views.detail, name="detail"),
    path('new/', b_views.new, name="new"),
    path('create/', b_views.create, name="create"),
    path('edit/<str:id>', b_views.edit, name="edit"),
    path('update/<str:id>', b_views.update, name="update"),
    path('delete/<str:id>', b_views.delete, name="delete"),
    path('list/', b_views.list, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
