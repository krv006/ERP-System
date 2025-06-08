from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER

# FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
FROM_EMAIL = EMAIL_HOST_USER


@shared_task
def send_verification_email(email, code):
    subject = "Your Verification Code"
    message = f"Your verification code is: {code}"
    from_email = FROM_EMAIL  # Change this
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
