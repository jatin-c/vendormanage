from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PurchaseOrder
from vendor.models import Vendor
from .serializers import PurchaseOrderSerializer
from django.utils.dateparse import parse_date

from django.http import Http404

class PurchaseOrderListCreateAPIView(APIView):
    def get(self, request):
        vendor_id = request.query_params.get('vendor_id')  # Extract vendor_id from query parameters
        if vendor_id:
            try:
                vendor = Vendor.objects.get(pk=vendor_id)
                purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)
                vendor_name = vendor.name  # Get the vendor's name
            except Vendor.DoesNotExist:
                raise Http404("Vendor does not exist")
        else:
            purchase_orders = PurchaseOrder.objects.all()
            vendor_name = None

        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        
        # Add vendor's name to the serialized data
        if vendor_id:
            return Response({"vendor_name": vendor_name, "purchase_orders": serializer.data})
        else:
            return Response({"purchase_orders": serializer.data})

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Purchase order has been placed successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get(self, request):
    #     vendor_id = request.query_params.get('vendor_id')  # Extract vendor_id from query parameters
    #     if vendor_id:
    #         try:
    #             vendor = Vendor.objects.get(pk=vendor_id)
    #             purchase_orders = PurchaseOrder.objects.filter(vendor=vendor)
    #         except Vendor.DoesNotExist:
    #             raise Http404("Vendor does not exist")
    #     else:
    #         purchase_orders = PurchaseOrder.objects.all()

    #     serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    #     return Response(serializer.data)


class PurchaseOrderRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, po_id):
        try:
            return PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return None

    def get(self, request, po_id):
        purchase_order = self.get_object(po_id)
        if purchase_order:
            serializer = PurchaseOrderSerializer(purchase_order)
            return Response({"message": "Purchase order details retrieved successfully", "data": serializer.data})
        return Response({"message": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)


    # def put(self, request, po_id):
    #     purchase_order = self.get_object(po_id)
    #     if purchase_order:
    #         serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, po_id):
        purchase_order = self.get_object(po_id)
        if purchase_order:
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, po_id):
        purchase_order = self.get_object(po_id)
        if purchase_order:
            purchase_order.delete()
            return Response({"message": "Purchase order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)



class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if acknowledgment_date is provided in the request data
        acknowledgment_date = request.data.get('acknowledgment_date')
        if acknowledgment_date is None:
            return Response({"error": "Acknowledgment date is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Update the acknowledgment_date of the purchase order
        purchase_order.acknowledgment_date = acknowledgment_date
        purchase_order.save()

        # Return success response
        return Response({"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)
