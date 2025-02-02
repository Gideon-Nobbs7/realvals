from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_yes_email(user_email, context):
    subject = "Proposal Acceptance"
    body = render_to_string("acceptance.html", context)

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [user_email],
        html_message=body,
        fail_silently=False
    )