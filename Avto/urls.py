from django.urls import path
from . import views
from .views import profile_edit_mode

urlpatterns = [
    path('', views.phone_list, name='phone-list'),
    path('phone-create/', views.phone_create, name='phone-create'),
    path('detail/<int:id>/', views.phone_detail, name='phone-detail'),
    path('delete/<int:id>/', views.phone_delete, name='phone-delete'),
    path('update/<int:pk>/', views.update_phone, name='phone-update'),#html yaratish kerak
    path('create/', views.create_phone, name='create'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.user_account, name='user-account'),
    path('account/edit/', profile_edit_mode, name='profile-edit'),
]
