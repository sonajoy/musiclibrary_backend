from django.urls import path
from . import views

urlpatterns = [
    path('song/', views.songListCreateView.as_view(), name='song-list-create'),
    path('song/<int:pk>/', views.songDetailView.as_view(), name='song-detail'),

]