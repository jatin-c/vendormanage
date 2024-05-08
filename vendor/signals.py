from datetime import datetime

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import F
from .models import Vendor, HistoricalPerformance

@receiver(pre_save, sender=Vendor)
def track_vendor_changes(sender, instance, **kwargs):
    # Retrieve the current instance from the database
    try:
        old_instance = Vendor.objects.get(pk=instance.pk)
    except Vendor.DoesNotExist:
        # If the instance is new, set old_instance to None
        old_instance = None
    
    # Initialize a list to store the names of changed fields
    instance.changed_fields = []
    
    # Compare each field value between the current and old instances
    if old_instance:
        if instance.on_time_delivery_rate != old_instance.on_time_delivery_rate:
            instance.changed_fields.append('on_time_delivery_rate')
        if instance.quality_rating_average != old_instance.quality_rating_average:
            instance.changed_fields.append('quality_rating_average')
        if instance.average_response_time != old_instance.average_response_time:
            instance.changed_fields.append('average_response_time')
        if instance.fulfillment_rate != old_instance.fulfillment_rate:
            instance.changed_fields.append('fulfillment_rate')

@receiver(post_save, sender=Vendor)
def update_historical_performance(sender, instance, **kwargs):
    # Check if any of the relevant fields have changed
    relevant_fields = ['on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']
    if any(field in instance.changed_fields for field in relevant_fields):
        # Create a new HistoricalPerformance instance
        historical_performance = HistoricalPerformance.objects.create(
            vendor=instance,
            date=datetime.now(),  # You may want to use timezone.now() if you're working with timezones
            on_time_delivery_rate=instance.on_time_delivery_rate,
            quality_rating_average=instance.quality_rating_average,
            average_response_time=instance.average_response_time,
            fulfillment_rate=instance.fulfillment_rate
        )
        historical_performance.save()
