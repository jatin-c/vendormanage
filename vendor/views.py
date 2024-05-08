from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from django.http import Http404

class VendorCreateAPIView(APIView):
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vendor created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class VendorListAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        if not vendors:
            return Response({"message": "There are no vendors available"}, status=status.HTTP_204_NO_CONTENT)
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    
class VendorRetrieveAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            raise Http404("Vendor does not exist")

    
class VendorUpdateAPIView(APIView):
    def put(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VendorDeleteAPIView(APIView):
    def delete(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            vendor_name = vendor.name  # Get the name of the vendor for the response message
            vendor.delete()
            return Response({"message": f"{vendor_name} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            raise Http404("Non-existing vendor cannot be deleted")

    
class VendorPerformance(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve performance metrics from the vendor instance
        performance_data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_average,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }

        return Response(performance_data, status=status.HTTP_200_OK)
    
class VendorPerformanceHistory(APIView):
    def get(self, request, vendor_id):
        # Query historical performance data for the specified vendor
        performance_history = HistoricalPerformance.objects.filter(vendor_id=vendor_id)

        # Check if historical performance data exists for the vendor
        if not performance_history.exists():
            return Response({"error": "No historical performance data found for the vendor"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize historical performance data
        serializer = HistoricalPerformanceSerializer(performance_history, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class HistoricalPerformanceListAPIView(APIView):
    def get(self, request, format=None):
        historical_performance_entries = HistoricalPerformance.objects.all()
        serializer = HistoricalPerformanceSerializer(historical_performance_entries, many=True)
        return Response(serializer.data)