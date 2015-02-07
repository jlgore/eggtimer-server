from django.core.mail import EmailMultiAlternatives
from email.utils import formataddr


def send(recipient, subject, text_body, html_body):
    recipients = [formataddr((recipient.get_full_name(), recipient.email))]
    msg = EmailMultiAlternatives(subject, text_body, to=recipients)
    if html_body:
        msg.attach_alternative(html_body, "text/html")
    msg.send()
