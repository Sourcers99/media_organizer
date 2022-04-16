
from django.urls import path
from videos import views

urlpatterns = [
    path('', views.index, name="index"),
    path('videos/', views.videos, name="videos"),
    path('video/<int:pk>', views.video, name="video"),
    path('categories/', views.categories, name="categories"),
    path('category/<int:pk>', views.category, name="category"),
    path('tags/', views.tags, name="tags"),
    path('tag/<int:pk>', views.tag, name="tag"),
    path('channels/', views.channels, name="channels"),
    path('channel/<int:pk>', views.channel, name="channel"),
    path('subsites/', views.subsites, name="subsites"),
    path('subsite/<int:pk>', views.tag, name="tag"),
    path('stars/', views.stars, name="stars"),
    path('star/<int:pk>', views.star, name="star"),
    path('settings/', views.settings, name="settings"),
    path('pending/', views.pending, name="pending"),
    path('save-settings/', views.save_settings, name="save-settings")
]
