import time
from celery import shared_task
from django.core.mail import EmailMessage
from datetime import date, timedelta
from django.template.loader import render_to_string
from django.conf import settings
from core.models import *

@shared_task
def dump_database():
    print('ise dusdu')
    time.sleep(100)
    print('dayandi')
    return True


@shared_task
def send_email_to_subscribers():
    user_emails = Subscriber.objects.values_list('email', flat=True) #'select email from subscribers '
    today = date.today()
    yesterday = today - timedelta(days=1)
    site_address = settings.SITE_ADDRESS
    

    template_name = 'email-subscribers.html'
    message = render_to_string(template_name, context)

    
    msg = EmailMessage(subject='Stoies daily digest', body=message, from_email=settings.EMAIL_HOST_USER, to=user_emails)

    msg.content_subtype = 'html'
    msg.send()