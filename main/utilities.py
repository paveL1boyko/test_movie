from django.core.signing import Signer
from django.template.loader import render_to_string

from lesson_temlate.settings import ALLOWED_HOSTS

signer = Signer()


def send_activations_notification(user):
    if ALLOWED_HOSTS:
        host = f'http://{ALLOWED_HOSTS[0]}'
    else:
        host = 'http://localhost:8000'

    context = dict(user=user, host=host, sign=signer.sign(user.username))
    subject = render_to_string('main/accounts/email/activation_letter_subject.txt', context)
    email_body = render_to_string('main/accounts/email/activation_letter_body.txt', context)
    user.email_user(subject, email_body)
