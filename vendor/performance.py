from purchase_order.models import PurchaseOrder
from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import Coalesce
from django.db.models import Sum
from datetime import timedelta


class PerformanceMetrics:
    def __init__(self, purchase_order: PurchaseOrder):
        self.purchase_order = purchase_order

    def calculate_on_time_delivery_rate(self):
        vendor = self.purchase_order.vendor

        # Filter completed purchase orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

        # Count the number of completed orders delivered on or before delivery_date
        on_time_orders = completed_orders.filter(delivery_date__lte=self.purchase_order.delivery_date).count()

        # Calculate the total number of completed orders for the vendor
        total_completed_orders = completed_orders.count()

        # Handle scenarios like missing data points or division by zero
        if total_completed_orders == 0:
            return 0
        else:
            # Calculate on-time delivery rate
            on_time_delivery_rate = (on_time_orders / total_completed_orders) * 100
            return round(on_time_delivery_rate, 2)  # Round to 2 decimal places

    def calculate_quality_rating_average(self):
        vendor = self.purchase_order.vendor

        # Filter completed purchase orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

        # Calculate the total number of completed orders
        total_completed_orders = completed_orders.count()

        if total_completed_orders == 0:
            return 0  # Return 0 if no completed orders

        # Calculate the sum of quality ratings for completed orders
        total_quality_rating = completed_orders.aggregate(total_quality_rating=Sum('quality_rating'))['total_quality_rating'] or 0

        # Calculate the average quality rating
        quality_rating_average = total_quality_rating / total_completed_orders

        return round(quality_rating_average, 2)  # Round to 2 decimal places

    def calculate_average_response_time(self):
        vendor = self.purchase_order.vendor

        # Filter purchase orders for the vendor
        purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)

        # Calculate time difference between issue_date and acknowledgment_date for each PO
        response_time_expression = ExpressionWrapper(
            F('acknowledgment_date') - F('issue_date'),
            output_field=fields.DurationField()
        )

        # Handle scenarios like missing data points
        response_time = Coalesce(response_time_expression, timedelta(seconds=0))

        # Calculate average response time in seconds
        total_response_time = purchase_orders.annotate(
            response_time=response_time
        ).aggregate(
            total_response_time=Sum('response_time')
        )['total_response_time'] or timedelta(seconds=0)

        total_po_count = purchase_orders.count()

        if total_po_count == 0:
            return 0  # Return 0 if no purchase orders

        # Calculate average response time in seconds
        average_response_time_seconds = total_response_time.total_seconds() / total_po_count

        return round(average_response_time_seconds, 2)

    def calculate_fulfillment_rate(self):
        vendor = self.purchase_order.vendor

        # Filter purchase orders for the vendor
        purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)

        # Count the number of successfully fulfilled purchase orders (status 'completed' without issues)
        successful_orders_count = purchase_orders.filter(status='completed').count()

        # Count the total number of purchase orders issued to the vendor
        total_orders_count = purchase_orders.count()

        if total_orders_count == 0:
            return 0  # Return 0 if no purchase orders

        # Calculate fulfillment rate
        fulfillment_rate = (successful_orders_count / total_orders_count) * 100

        return round(fulfillment_rate, 2)
