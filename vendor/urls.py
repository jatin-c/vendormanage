from django.urls import path
from .views import (
    VendorCreateAPIView,
    VendorListAPIView,
    VendorRetrieveAPIView,
    VendorUpdateAPIView,
    VendorDeleteAPIView,
    VendorPerformance,
    VendorPerformanceHistory,
    HistoricalPerformanceListAPIView
,
)

urlpatterns = [
    path('', VendorListAPIView.as_view(), name='vendor-list'),
    path('create/', VendorCreateAPIView.as_view(), name='vendor-create'),
    path('<int:vendor_id>/', VendorRetrieveAPIView.as_view(), name='vendor-retrieve'),
    path('<int:vendor_id>/update/', VendorUpdateAPIView.as_view(), name='vendor-update'),
    path('<int:vendor_id>/delete/', VendorDeleteAPIView.as_view(), name='vendor-delete'),
    path('<int:vendor_id>/performance/', VendorPerformance.as_view(), name='vendor_performance'),
    path('<int:vendor_id>/performancehistory/', VendorPerformanceHistory.as_view(), name='vendor_performance_history'),
    path('historicalperformance/listall/', HistoricalPerformanceListAPIView.as_view(), name='historical_performance_list'),

]


