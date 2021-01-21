from django.urls import path
from .views import register, profileView, publicProfileView, userLogin, userLogout

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profileView, name='profile'),
    path('profile/<str:username>/', publicProfileView, name='public-profile'),
    path('login/', userLogin.as_view(), name='login'),
    path('logout/', userLogout, name='logout'),
]