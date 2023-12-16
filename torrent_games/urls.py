from django.urls import path
from .views import *

urlpatterns = [
    path('', GamesListView.as_view(), name='index'),
    path('category/<int:pk>', GamesListByCategory.as_view(), name='category'),
    path('game/<int:pk>', GamesDownload.as_view(), name='game'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
    path('save_comment/<int:pk>/', save_comment, name='save_comment'),
    path('download/<int:pk>/', download_file, name='download_file'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('edit_account/', edit_account_view, name='edit_account'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),
]
