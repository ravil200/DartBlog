from django.urls import URLPattern, path 
from .views import Home, GetPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>', GetPost.as_view(), name='Post'),
]