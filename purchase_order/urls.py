from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, AcknowledgePurchaseOrder

urlpatterns = [
    path('', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('<int:po_id>', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('<int:po_id>/acknowledge', AcknowledgePurchaseOrder.as_view(), name='acknowledge_purchase_order'),
]

