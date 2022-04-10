
from django.urls import path
from videos import views

urlpatterns = [
    path('', views.index, name="index"),
    path('settings', views.settings, name="settings")
]
