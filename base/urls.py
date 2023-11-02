from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author/<str:pk>/', views.authorPage, name='author'),
    
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    path('create-blog/', views.createBlog, name='create-blog'),
    path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    
    path('blog/<str:pk>/', views.blog, name='blog'),
    path('create-word/<str:pk>/', views.createWord, name='create-word'),
    
    path('my-vocabulary/', views.myVocabs, name='my-vocabulary'),
]
