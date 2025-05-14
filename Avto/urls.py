from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_list, name='phone-list'),
    path('phone-create/', views.phone_create, name='phone-create'),
    path('detail/<int:id>/', views.phone_detail, name='phone-detail'),
    path('delete/<int:id>/', views.phone_delete, name='phone-delete'),
    path('update/<int:pk>/', views.update_phone, name='phone-update'),#html yaratish kerak
    path('create/', views.create_phone, name='create'),
]
