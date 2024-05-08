from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import PurchaseOrder
from vendor.models import Vendor
from .performance import PerformanceMetrics 
# performance_metrics = PerformanceMetrics()

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, created, **kwargs):
    if not created:
        # Calculate on-time delivery rate
        if instance.status == 'completed':
            performance_metrics = PerformanceMetrics(instance)
            on_time_delivery_rate = performance_metrics.calculate_on_time_delivery_rate()
            try:
                # Retrieve Vendor instancee
                vendor = Vendor.objects.get(pk=instance.vendor_id)
            except Vendor.DoesNotExist:
                # Handle the case where the vendor does not exist
                print(f"Vendor with ID {instance.vendor_id} does not exist.")
            else:
                # Update Vendor model with the new on-time delvery rate
                vendor.on_time_delivery_rate = on_time_delivery_rate
                vendor.save()

        # # Calculate fulfillment rate
        # performance_metrics = PerformanceMetrics(instance)
        # fulfillment_rate = performance_metrics.calculate_fulfillment_rate()
        # try:
        #     # Retrieve Vendor instance
        #     vendor = Vendor.objects.get(pk=instance.vendor_id)
        # except Vendor.DoesNotExist:
        #     # Handle the case where the vendor does not exist
        #     print(f"Vendor with ID {instance.vendor_id} does not exist.")
        # else:
        #     # Update Vendor model with the new fulfillment rate
        #     vendor.fulfillment_rate = fulfillment_rate
        #     vendor.save()

@receiver(pre_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    try:
        # Retrieve the previous instance from the database
        previous_instance = PurchaseOrder.objects.get(pk=instance.pk)

        # Check if status field has changed
        if instance.pk and instance.status != previous_instance.status:
            # Calculate fulfillment rate
            performance_metrics = PerformanceMetrics(instance)
            fulfillment_rate = performance_metrics.calculate_fulfillment_rate()
            try:
                # Retrieve Vendor instance
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.fulfillment_rate = fulfillment_rate
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")
    except PurchaseOrder.DoesNotExist:
        # For new instances
        pass


@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_average(sender, instance, created, **kwargs):
    if not created:  
        if instance.quality_rating is not None:  # it Checks if a quality rating is provided
            # Calculate quality rating average
            performance_metrics = PerformanceMetrics(instance)
            quality_rating_average = performance_metrics.calculate_quality_rating_average()

            # Update Vendor model with the new quality rating average
            try:
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.quality_rating_average = quality_rating_average
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")

@receiver(pre_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    try:
        # Retrieve the previous instance from the database
        previous_instance = PurchaseOrder.objects.get(pk=instance.pk)

        # Check if acknowledgment_date has changed
        if instance.acknowledgment_date != previous_instance.acknowledgment_date:
            # Calculate average response time
            performance_metrics = PerformanceMetrics(instance)
            average_response_time = performance_metrics.calculate_average_response_time()

            # Update Vendor model with the new average response time
            try:
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.average_response_time = average_response_time
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")
    except PurchaseOrder.DoesNotExist:
        # For new instances
        pass

