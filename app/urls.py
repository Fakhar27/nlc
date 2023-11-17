from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views



urlpatterns = [
    path('',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('dash/',views.dash,name="dash"),
    path('showdata/',views.showdata,name="showdata"),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
