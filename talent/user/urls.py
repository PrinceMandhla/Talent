from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginView,name='login'),
    path('reg/',views.regView,name='reg'),
    path('logout/',views.logoutView,name='logout')
]