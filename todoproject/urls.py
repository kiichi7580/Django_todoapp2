"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from todoapp.views import CustomLoginView, todoapp, todo_post, todo_delete
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from todoapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CustomLoginView.as_view(), name="index"),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),

    path("todo/", todoapp),
    path("todo_post/", todo_post),
    path("delete/<int:task_id>", todo_delete),
]


