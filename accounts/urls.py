from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
#     path('<int:username>/', views.detail, name='detail'),
#     path('<int:username>/result', views.result, name='result'),
#     path('<int:username>/nickname', views.nickname, name='nickname'),
]