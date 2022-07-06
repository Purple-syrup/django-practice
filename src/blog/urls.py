from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
] + router.urls 

#127.0.0.1:8007/posts