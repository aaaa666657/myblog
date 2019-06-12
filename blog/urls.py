from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('create', views.addteacher, name='addteacher'),
    path('sign-up', views.UserCreate.as_view(), name='sign_up'),
    path('class',views.showclass, name='showclass'),
]

