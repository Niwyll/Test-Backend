from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from .models import IceCreamBucket

@receiver(post_save, sender=IceCreamBucket)
def notify_admin_when_empty(sender, instance, **kwargs):
    """Send an email to admin when an IceCreamBucket is empty."""
    if instance.quantity == 0:
        subject = f"🚨 Ice Cream Bucket Empty: {instance.ice_cream.name}"
        message = (
            f"The bucket for {instance.ice_cream.name} is empty.\n"
            f"Total Capacity: {instance.initial_quantity} balls.\n"
            f"Please refill it immediately at http://localhost:8000{reverse('icecreams:management-buckets')}."
        )

        admin_email = "admin@icecreamseller.com"
        print(f"Sending {subject} to {admin_email}")
        print(message)