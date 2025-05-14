from django.urls import path

from accounts import views
# from Avto.views import phone_list


urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
