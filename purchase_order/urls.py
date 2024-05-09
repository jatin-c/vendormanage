from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, AcknowledgePurchaseOrder

urlpatterns = [
    # path('', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('listall/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list'),
    path('create/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-create'),
    path('<int:po_id>/get/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve'),
    path('<int:po_id>/update/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-update'),
    path('<int:po_id>/delete/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-destroy'),
    path('<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge_purchase_order'),
]

