from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_account, name="register"),
    path('login/', views.login_account, name="login"),
    path('logout/', views.logout_account, name="logout"),
    path('review/', views.review_account, name="review"),
]
