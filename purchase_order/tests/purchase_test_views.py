from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from purchase_order.models import PurchaseOrder
from vendor.models import Vendor

class PurchaseOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a vendor
        self.vendor = Vendor.objects.create(name="Test Vendor")

        # Create some sample purchase orders
        PurchaseOrder.objects.create(
            vendor=self.vendor,
            po_number="PO001",
            order_date="2024-05-09T00:00:00",  # Adjusted date format
            issue_date="2024-05-09T00:00:00",   # Adjusted date format
            delivery_date="2024-05-09T00:00:00", # Adjusted date format
            items=["Item 1", "Item 2"],          # Adjusted to include items
            quantity=10,                         # Adjusted to include quantity
            status="Pending",                    # Adjusted to include status
        )

    def test_list_purchase_orders(self):
        response = self.client.get(reverse('purchase-order-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['purchase_orders']), 1)  # Assuming one purchase order created in setUp

    def test_create_purchase_order(self):
        data = {
            'vendor': self.vendor.pk,
            'po_number': 'PO002',                 # Added PO number
            'order_date': '2024-05-09T00:00:00',  # Adjusted date format
            'issue_date': '2024-05-09T00:00:00',  # Adjusted date format
            'delivery_date': '2024-05-09T00:00:00', # Adjusted date format
            'items': ["Item 3", "Item 4"],        # Added items
            'quantity': 20,                       # Added quantity
            'status': 'Pending',                  # Added status
        }
        response = self.client.post(reverse('purchase-order-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)  # Assuming this is the second object created

    # You can add more test cases for different scenarios


    class PurchaseOrderRetrieveUpdateDestroyAPITestCase(TestCase):
        def setUp(self):
            self.client = APIClient()
            self.vendor = Vendor.objects.create(name="Test Vendor")
            self.purchase_order = PurchaseOrder.objects.create(
                vendor=self.vendor,
                po_number="PO001",
                order_date="2024-05-09T00:00:00",
                issue_date="2024-05-09T00:00:00",
                delivery_date="2024-05-09T00:00:00",
            )

        def test_retrieve_purchase_order(self):
            response = self.client.get(reverse('purchase-order-retrieve', kwargs={'po_id': self.purchase_order.pk}))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_update_purchase_order(self):
            data = {
                'order_date': '10/05/2024',  # Change the order date
            }
            response = self.client.put(reverse('purchase-order-update', kwargs={'po_id': self.purchase_order.pk}), data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(PurchaseOrder.objects.get(pk=self.purchase_order.pk).order_date.strftime('%d/%m/%Y'), '10/05/2024')

        def test_delete_purchase_order(self):
            response = self.client.delete(reverse('purchase-order-destroy', kwargs={'po_id': self.purchase_order.pk}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(PurchaseOrder.objects.filter(pk=self.purchase_order.pk).exists())



class AcknowledgePurchaseOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name="Test Vendor")
        self.purchase_order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            po_number="PO001",
            order_date="2024-05-09T00:00:00",
            issue_date="2024-05-09T00:00:00",
            delivery_date="2024-05-09T00:00:00",
        )

    def test_acknowledge_purchase_order(self):
        response = self.client.put(reverse('acknowledge_purchase_order', kwargs={'po_id': self.purchase_order.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)

    def test_acknowledge_nonexistent_purchase_order(self):
        response = self.client.put(reverse('acknowledge_purchase_order', kwargs={'po_id': 999}))  # Nonexistent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)