from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vendor, HistoricalPerformance
from datetime import datetime

@receiver(post_save, sender=Vendor)
def update_historical_performance(sender, instance, **kwargs):
    # Check if any of the performance fields have changed
    if any(field.attname in instance.changed_data for field in instance._meta.get_fields() if field.attname in ['on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfillment_rate']):
        # Create a new HistoricalPerformance instance
        historical_performance = HistoricalPerformance.objects.create(
            vendor=instance,
            date=datetime.now(),
            on_time_delivery_rate=instance.on_time_delivery_rate,
            quality_rating_average=instance.quality_rating_average,
            average_response_time=instance.average_response_time,
            fulfillment_rate=instance.fulfillment_rate
        )
        historical_performance.save()
