from django.urls import path
from .views import registrar_usuario, loginPage , logoutuser, profile

urlpatterns = [
    path('newuser', registrar_usuario, name='register'),
    path('login',loginPage,name='login'),
    path('logout',logoutuser,name='logout'),
    path('profile',profile,name='profile')

]
