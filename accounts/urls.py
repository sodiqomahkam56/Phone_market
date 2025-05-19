from django.urls import path
from accounts import views
from accounts.utils import send_html_email
from accounts.views import send_email, forget_view, change_password_view

urlpatterns = [
    path('html-email/', send_email, name='email'),
    path('', send_html_email, name='html-email'),
    path('login/', views.login_view, name='login'),
    path('forget/', forget_view, name='forget'),
    path('change/', change_password_view, name='change-password'),
    path('register/', views.register, name='register'),
]
