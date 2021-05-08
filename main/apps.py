from django.apps import AppConfig
from django.dispatch import Signal, receiver

from .utilities import send_activations_notification

user_registered = Signal()


@receiver(user_registered)
def user_registered_dispatcher(sender, **kwargs):
    send_activations_notification(kwargs['instance'])


# user_registered.connect(user_registered_dispatcher)


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'главная'
