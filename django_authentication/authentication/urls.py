from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('index', user_home, name="user_home"),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
