# PurchaseOrderListAPIView(PurchaseOrderListCreateAPIView)
## URL 
- Endpoint: api/purchase_order/listall/
- Endpoint :api/purchase_order/listall/?vendor=vendor_id (filters the list of purchase_order by vendor)
### Method: GET
## Description
- Retrieves a list of purchase orders.
### If a vendor_id query parameter is provided, retrieves purchase orders associated with that vendor; otherwise, retrieves all purchase orders.
### Optionally returns the vendor's name along with the list of purchase orders if a vendor_id is provided.
## Parameters
### vendor_id (optional): ID of the vendor to filter purchase orders by.

- ```json
  {
  "vendor_name": "Vendor Name",
  "purchase_orders": [
    {
      "po_number": "PO123",
      "vendor": 123,
      "order_date": "2024-05-09T12:00:00Z",
      "delivery_date": "2024-05-16T12:00:00Z",
      "items": ["Item1", "Item2"],
      "quantity": 10,
      "status": "Pending",
      "quality_rating": null,
      "issue_date": "2024-05-09T12:00:00Z",
      "acknowledgment_date": null
    },
    {
      "po_number": "PO124",
      "vendor": 123,
      "order_date": "2024-05-10T12:00:00Z",
      "delivery_date": "2024-05-17T12:00:00Z",
      "items": ["Item3", "Item4"],
      "quantity": 5,
      "status": "Delivered",
      "quality_rating": 4.5,
      "issue_date": "2024-05-10T12:00:00Z",
      "acknowledgment_date": "2024-05-15T12:00:00Z"
    }
  ]
  
# CreatePurchaseOrderAPIView (PurchaseOrderListCreateAPIView)
## URL
- Endpoint: api/purchase_order/create/
### Method: POST
- Description
### Creates a new purchase order.
### Requires authentication.
- Expects the request body to contain details of the purchase order including PO number, vendor ID, order date, delivery date, items, quantity, status, and optionally issue date.
## Parameters
- po_number: Purchase order number (string, required)
- vendor: Vendor ID (integer, required)
- order_date: Order date in "day/month/year" format (string, required)
- delivery_date: Delivery date in "day/month/year" format (string, required)
- items: List of items (array, required)
- quantity: Quantity of items (integer, required)
- status: Status of the order (string, required)
- quality_rating: Quality rating (float, optional)
- issue_date: Issue date in "day/month/year" format (string, optional)
# Example
`POST api/purchase_order/create/`
 - ```json
    {
      "po_number": "PO125",
      "vendor": 123,
      "order_date": "09/05/2024",
      "delivery_date": "16/05/2024",
      "items": ["Item5", "Item6"],
      "quantity": 8,
      "status": "Pending",
      "issue_date": "09/05/2024"
    }
### Response
- ```json
  {
    "message": "Purchase order has been placed successfully",
    "data": {
      "po_number": "PO125",
      "vendor": 123,
      "order_date": "2024-05-09T00:00:00Z",
      "delivery_date": "2024-05-16T00:00:00Z",
      "items": ["Item5", "Item6"],
      "quantity": 8,
      "status": "Pending",
      "quality_rating": null,
      "issue_date": "2024-05-09T00:00:00Z",
      "acknowledgment_date": null
    }
  }

# PurchaseOrderRetrieveUpdateDestroyAPIView
## Description:
- This API endpoint allows authenticated users to retrieve, update, or delete a specific purchase order.

### Endpoint:
- Retrieve: api/purchase_order/<po_id>/get/
- Update: api/purchase_order/<po_id>/update/
- Destroy: api/purchase_order/<po_id>/delete/
### Request Type:
- GET (Retrieve)
- PUT (Update)
- DELETE (Destroy)
### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.
## Retrieve Purchase Order (GET)
### Parameters:
- po_id: ID of the purchase order to retrieve.
### Example Request:
`GET api/purchase_order/123/get/`
### Response:
- ```json
    {
      "message": "Purchase order details retrieved successfully",
      "data": {
        "po_number": "PO123",
        "vendor": 123,
        "order_date": "2024-05-09T12:00:00Z",
        "delivery_date": "2024-05-16T12:00:00Z",
        "items": ["Item1", "Item2"],
        "quantity": 10,
        "status": "Pending",
        "quality_rating": null,
        "issue_date": "2024-05-09T12:00:00Z",
        "acknowledgment_date": null
      }
    }
  
# Update Purchase Order (PUT)
## Parameters:
- po_id: ID of the purchase order to update.
### Example JSON Payload:
`PUT api/purchase_order/123/update/`
- ```json
    {
      "po_number": "PO123",
      "vendor": 123,
      "order_date": "09/05/2024",
      "delivery_date": "16/05/2024",
      "items": ["Item1", "Item2"],
      "quantity": 10,
      "status": "Pending",
      "issue_date": "09/05/2024",
      "acknowledgment_date": null
    }
## Response:
### Success Response (200):
- ```json
  { "message": "Purchase order updated successfully", "data": { ... } }
- Error Response (400):

- ```json
  { "error": "Error details specifying which fields failed validation" }
# Delete Purchase Order (DELETE)
## Parameters:
- po_id: ID of the purchase order to delete.
### Example Request:

`DELETE api/purchase_order/123/delete/`
### Response:
- Success Response (204):

- ```json
  { "message": "Purchase order deleted successfully" }

# AcknowledgePurchaseOrder
## Description:
- This API endpoint allows authenticated users to acknowledge a purchase order.

## Endpoint:
- URL: api/purchase_order/<po_id>/acknowledge/
### Request Type: PUT
### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.
## Acknowledge Purchase Order (PUT)
### Parameters:
- po_id: ID of the purchase order to acknowledge.
### Example Request:
`PUT api/purchase_order/123/acknowledge/
## Response:
### Success Response (200):

- ```json
  { "message": "Purchase order acknowledged successfully" }
### Error Response (404):
- ```json
  { "error": "Purchase order not found" }


# update_vendor_metrics Signal (on_time_delivery_rate)
## Description:
- This signal function is triggered after a PurchaseOrder instance is saved. It updates the performance metrics of the associated vendor, particularly the on-time delivery rate.

## Functionality:
- Calculate On-time Delivery Rate: Checks if the PurchaseOrder status is 'completed' and calculates the on-time delivery rate using the PerformanceMetrics class. 
- Update Vendor Metrics: Retrieves the associated Vendor instance and updates its on-time delivery rate with the newly calculated value.
- ```python
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

## Execution:
- This signal function is executed after a PurchaseOrder instance is saved.
- It checks if the order status is 'completed' and calculates the on-time delivery rate.
- Then, it retrieves the associated vendor and updates its on-time delivery rate.

# update_fulfillment_rate Signal
## Description:
- This signal function is triggered before a PurchaseOrder instance is saved. It updates the fulfillment rate of the associated vendor based on changes in the order status.

## Functionality:
- Retrieve Previous Instance: Retrieves the previous instance of the PurchaseOrder from the database.
- ```python
  previous_instance = PurchaseOrder.objects.get(pk=instance.pk)
- Check Status Change: Compares the status of the current instance with the previous one to detect changes.
- ```python
  if instance.pk and instance.status != previous_instance.status:
- Calculate Fulfillment Rate: If the status has changed, calculates the fulfillment rate using the PerformanceMetrics class.
- ```python
  performance_metrics = PerformanceMetrics(instance)
  fulfillment_rate = performance_metrics.calculate_fulfillment_rate()
- Update Vendor Metrics: Retrieves the associated Vendor instance and updates its fulfillment rate with the newly calculated value.
- ```python
  try:
                # Retrieve Vendor instance
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.fulfillment_rate = fulfillment_rate
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")
## Execution:
- This signal function is executed before a PurchaseOrder instance is saved.
- It retrieves the previous instance to compare status changes.
- If the status has changed, it calculates the fulfillment rate and updates the associated vendor.

# update_quality_rating_average Signal
## Description:
-This signal function is triggered after a PurchaseOrder instance is saved. It updates the quality rating average of the associated vendor based on the quality rating provided in the purchase order.

## Functionality:
- Check Quality Rating: Checks if a quality rating is provided for the purchase order.
- ```python
  if not created:  
        if instance.quality_rating is not None:  # it Checks if a quality rating is provided
- Calculate Quality Rating Average: If a quality rating is provided, calculates the quality rating average using the PerformanceMetrics class.
- ```python
  # Calculate quality rating average
            performance_metrics = PerformanceMetrics(instance)
            quality_rating_average = performance_metrics.calculate_quality_rating_average()
- Update Vendor Metrics: Retrieves the associated Vendor instance and updates its quality rating average with the newly calculated value.
- ```python
   try:
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.quality_rating_average = quality_rating_average
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")

# update_average_response_time Signal
## Description:
- This signal function is triggered before a PurchaseOrder instance is saved. It updates the average response time of the associated vendor based on changes in the acknowledgment date of the purchase order.

## Functionality:
- Retrieve Previous Instance: Retrieves the previous instance of the PurchaseOrder from the database.
- ```python
  # Retrieve the previous instance from the database
        previous_instance = PurchaseOrder.objects.get(pk=instance.pk)
- Check Acknowledgment Date Change: Compares the acknowledgment date of the current instance with the previous one to detect changes.
- ```python
  if instance.acknowledgment_date != previous_instance.acknowledgment_date:
            
- Calculate Average Response Time: If the acknowledgment date has changed, calculates the average response time using the PerformanceMetrics class.
- ```python
  # Calculate average response time
            performance_metrics = PerformanceMetrics(instance)
            average_response_time = performance_metrics.calculate_average_response_time()
- Update Vendor Metrics: Retrieves the associated Vendor instance and updates its average response time with the newly calculated value.
- ```python
    try:
                vendor = Vendor.objects.get(pk=instance.vendor_id)
                vendor.average_response_time = average_response_time
                vendor.save()
            except Vendor.DoesNotExist:
                print(f"Vendor with ID {instance.vendor_id} does not exist.")
    except PurchaseOrder.DoesNotExist:



  




