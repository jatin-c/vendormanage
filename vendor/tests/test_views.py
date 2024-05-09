from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from vendor.models import Vendor
from vendor.serializers import VendorSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

class VendorCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))

    def test_create_vendor(self):
        data = {
            'name': 'Test Vendor',
            'contact_details': 'Contact Details',
            'address': 'Test Address',
            'vendor_code': 'VENDOR001',
            'on_time_delivery_rate': 0.9,
            'quality_rating_average': 4.5,
            'average_response_time': 12.5,
            'fulfillment_rate': 0.85
            # Add other fields as needed
        }
        response = self.client.post(reverse('vendor-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Vendor.objects.filter(name='Test Vendor').exists())

    def test_create_vendor_invalid_data(self):
        # Test case for creating a vendor with invalid data
        data = {
            # Invalid data, missing required fields or incorrect format
        }
        response = self.client.post(reverse('vendor-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class VendorListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
        Vendor.objects.create(name='Vendor 1', vendor_code='VENDOR001')
        Vendor.objects.create(name='Vendor 2', vendor_code='VENDOR002')

    def test_list_vendors(self):
        response = self.client.get(reverse('vendor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming 2 vendors are created in setUp

    def test_list_no_vendors(self):
        # Test case for listing vendors when there are no vendors available
        Vendor.objects.all().delete()  # Delete all vendors
        response = self.client.get(reverse('vendor-list'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




class VendorRetrieveAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Details',
            address='Test Address',
            vendor_code='VENDOR001',
            on_time_delivery_rate=0.9,
            quality_rating_average=4.5,
            average_response_time=12.5,
            fulfillment_rate=0.85
        )

    def test_retrieve_vendor(self):
        response = self.client.get(reverse('vendor-retrieve', kwargs={'vendor_id': self.vendor.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Vendor')
        self.assertEqual(response.data['contact_details'], 'Contact Details')
        self.assertEqual(response.data['address'], 'Test Address')
        self.assertEqual(response.data['vendor_code'], 'VENDOR001')
        self.assertEqual(response.data['on_time_delivery_rate'], 0.9)
        self.assertEqual(response.data['quality_rating_average'], 4.5)
        self.assertEqual(response.data['average_response_time'], 12.5)
        self.assertEqual(response.data['fulfillment_rate'], 0.85)

    def test_retrieve_nonexistent_vendor(self):
        response = self.client.get(reverse('vendor-retrieve', kwargs={'vendor_id': 999}))  # Nonexistent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class VendorUpdateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='Contact Details',
            address='Test Address',
            vendor_code='VENDOR001',
            on_time_delivery_rate=0.9,
            quality_rating_average=4.5,
            average_response_time=12.5,
            fulfillment_rate=0.85
        )

    def test_update_vendor(self):
        data = {
            'name': 'Updated Vendor Name',
            'contact_details': 'Updated Contact Details',
            'address': 'Updated Test Address',
            'vendor_code': 'VENDOR002',
            'on_time_delivery_rate': 0.95,
            'quality_rating_average': 4.8,
            'average_response_time': 10.5,
            'fulfillment_rate': 0.9
            # Add other fields as needed
        }
        response = self.client.put(reverse('vendor-update', kwargs={'vendor_id': self.vendor.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).name, 'Updated Vendor Name')
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).contact_details, 'Updated Contact Details')
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).address, 'Updated Test Address')
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).vendor_code, 'VENDOR002')
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).on_time_delivery_rate, 0.95)
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).quality_rating_average, 4.8)
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).average_response_time, 10.5)
        self.assertEqual(Vendor.objects.get(pk=self.vendor.pk).fulfillment_rate, 0.9)

    def test_update_nonexistent_vendor(self):
        data = {
            'name': 'Updated Vendor Name',
            'contact_details': 'Updated Contact Details',
            'address': 'Updated Test Address',
            'vendor_code': 'VENDOR002',
            'on_time_delivery_rate': 0.95,
            'quality_rating_average': 4.8,
            'average_response_time': 10.5,
            'fulfillment_rate': 0.9
            # Add other fields as needed
        }
        response = self.client.put(reverse('vendor-update', kwargs={'vendor_id': 999}), data, format='json')  # Nonexistent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class VendorDeleteAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
        self.vendor = Vendor.objects.create(name='Test Vendor')

    def test_delete_vendor(self):
        response = self.client.delete(reverse('vendor-delete', kwargs={'vendor_id': self.vendor.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vendor.objects.filter(pk=self.vendor.pk).exists())

    def test_delete_nonexistent_vendor(self):
        response = self.client.delete(reverse('vendor-delete', kwargs={'vendor_id': 999}))  # Nonexistent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class VendorPerformanceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Generate JWT access token
        access_token = AccessToken.for_user(self.user)

        # Set the authentication token in the client
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token))
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            on_time_delivery_rate=0.9,
            quality_rating_average=4.5,
            average_response_time=12.5,
            fulfillment_rate=0.85
        )

    def test_get_vendor_performance(self):
        response = self.client.get(reverse('vendor_performance', kwargs={'vendor_id': self.vendor.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['on_time_delivery_rate'], 0.9)
        self.assertEqual(response.data['quality_rating_average'], 4.5)
        self.assertEqual(response.data['average_response_time'], 12.5)
        self.assertEqual(response.data['fulfillment_rate'], 0.85)

    def test_get_performance_nonexistent_vendor(self):
        response = self.client.get(reverse('vendor_performance', kwargs={'vendor_id': 999}))  # Nonexistent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

