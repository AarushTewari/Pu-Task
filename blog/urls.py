from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddBlogView.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name='update-blog'),
    path('blog/remove/<int:pk>', DeleteBlogView.as_view(), name='delete-blog'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]