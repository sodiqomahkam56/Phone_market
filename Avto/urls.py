from django.urls import path
from . import views
from .views import profile_edit_mode
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.phone_list, name='phone-list'),
    path('phone-create/', views.phone_create, name='create'),
    path('detail/<int:id>/', views.phone_detail, name='phone-detail'),
    path('delete/<int:id>/', views.phone_delete, name='phone-delete'),
    path('update/<int:pk>/', views.update_phone, name='phone-update'),#html yaratish kerak
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.user_account, name='user-account'),
    path('account/edit/', profile_edit_mode, name='profile-edit'),
    path('toggle-favorite/<int:product_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('favorites/', views.favorites_list, name='favorites-list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
