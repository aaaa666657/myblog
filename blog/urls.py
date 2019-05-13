from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create', views.post_create, name='post_create'),
    path('sign-up', views.UserCreate.as_view(), name='sign_up'),
]

