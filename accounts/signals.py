from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser
from accounts.utils import send_html_email


@receiver(post_save, sender=CustomUser)
def create_customuser(sender, instance, created, **kwargs):
    if created:
        send_html_email(
            subject='Ro‘yxatdan o‘tdingiz',
            from_email=settings.EMAIL_HOST_USER,
            to_email="aliyer.temur95@gmail.com",
            verification_code="123456",
            username=instance.username
        )
        print("✅ Email yuborildi")
