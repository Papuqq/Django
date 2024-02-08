from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Post, UserResponse


@receiver (pre_save, sender=UserResponse)
def my_handler(sender, instance, created, **kwargs):
    if instance.status:
        mail = instance.author.email
        send_mail(
            subject=f'Обновлена новость {instance.article.category}',
            message=f'Новость: {instance.article.title}\n'
                    f'Ссылка на новость: http://127.0.0.1:8000{instance.article.get_absolute_url()}',
            from_email=None,
            fail_silently=False,
            recipient_list=[mail]
        )
    mail = instance.article.author.email
    send_mail(
    f'Новая новость: {instance.title}\n'
    f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
