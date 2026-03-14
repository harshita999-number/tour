from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from datetime import time
from datetime import timedelta
import random

from .models import roomBook, Booknow, Contact



# Random hotel list
HOTEL_LIST = ["Hotel Sunshine", "Hotel Paradise", "Hotel Moonlight", "Hotel Royal"]

# ---------------- Hotel Booking ----------------
@receiver(post_save, sender=roomBook)
def send_hotel_booking_email(sender, instance, created, **kwargs):
    if created and instance.payment_status == "Paid":
        # Random hotel assign if hotel field is empty
        hotel_name = random.choice(HOTEL_LIST)

        subject = "Hotel Booking Confirmation"
        message = f"""
Hello {instance.your_name},

Your hotel booking details:

Hotel Name: {hotel_name}
Check-in: {instance.checkin}
Check-out: {instance.checkout}
Guests: {instance.guests}

Thank you for using our service!
"""
        #from_email = 'hy99933@gmail.com'
        recipient_list = [instance.your_email]  # user form email

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            print(f"Email sent to {instance.your_email}")
            instance.email_status = 'Sent'
        except Exception as e:
            print(f"Email failed for {instance.your_email}: {e}")
            instance.email_status = 'Unsent'

        instance.save(update_fields=["email_status"])

# ---------------- Taxi Booking ----------------
@receiver(post_save, sender=Booknow)
def send_taxi_booking_email(sender, instance, created, **kwargs):
    if created and instance.payment_status == "Paid":
        hour = random.randint(6, 22)
        minute = random.randint(0, 50)
        arrival_time = time(hour, minute)
        subject = "Taxi Booking Confirmation"
        message = f"""
Hello {instance.user.username},

Your taxi booking details:

Destination: {instance.place}
Members: {instance.member_count}
Date: {instance.event_date}
Taxi Arrival Time: {arrival_time}

Thank you!
"""
        #from_email = 'hy99933@gmail.com'
        recipient_list = [instance.user.email]  # registered user email

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            print(f"Email sent to {instance.user.email}")
            instance.email_status = 'Sent'
        except Exception as e:
            print(f"Email failed for {instance.user.email}: {e}")
            instance.email_status = 'Unsent'

        instance.save(update_fields=["email_status"])

# ---------------- Contact Us ----------------
@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    print("signal triggered")
    if created:
        print("contact created")
        subject = "Thank You For Contacting Us"
        message = f"""
Hello {instance.username},

Thank you for contacting us. We have received your feedback and our team will process it soon.

We will get back to you soon!
"""
        #from_email = 'hy99933@gmail.com'
        recipient_list = [instance.my_email]  # user form email

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            print(f"Email sent to {instance.my_email}")
            instance.email_status = 'Sent'
        except Exception as e:
            print(f"Email failed for {instance.my_email}: {e}")
            instance.my_email_status = 'Unsent'

        instance.save(update_fields=["email_status"])

