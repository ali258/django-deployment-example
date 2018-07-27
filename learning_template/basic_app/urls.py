
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('registration/', views.register, name='reg'),
    path('logout/', views.user_logout,name='logout'),
    path('user_login/', views.user_login, name='user_login')
]
