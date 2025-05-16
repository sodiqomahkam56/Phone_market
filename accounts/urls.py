from django.urls import path
from accounts import views
from accounts.utils import send_html_email
from accounts.views import send_email

urlpatterns = [
    path('html-email/', send_email, name='email'),
    path('', send_html_email, name='html-email'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
