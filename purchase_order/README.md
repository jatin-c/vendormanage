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
  [
   {
  "vendor_name": "Vendor Name",
  "purchase_orders": [
    {
      "po_number": "PO123",
      "vendor": 123,
      "order_date": "2024-05-09T12:00:00Z",
      "delivery_date": "2024-05-16T12:00:00Z",
      "items": {
                "name": "Item 1",
                "quantity": 1,
                "price": 10.0
            },
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
      "items": {
                "name": "Item 1",
                "quantity": 1,
                "price": 10.0
            },
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
    'vendor': vendor_id,  # Assuming self.vendor is an instance of Vendor
    'po_number': 'PO002',
    'order_date': '09/05/2024',  
    'issue_date': '09/05/2024',  
    'delivery_date': '09/05/2024', 
    'items': {
        "name": "Item 1",
        "quantity": 1,
        "price": 10.0
    },        # Added items
    'quantity': 20,             
    'status': 'Pending',       
    'quality_rating': None,    
    'acknowledgment_date': None 
   }
### Response
- ```json
  {
  'vendor': vendor_id,  
  'po_number': 'PO002',       
  'order_date': '09/05/2024', 
  'issue_date': '09/05/2024',  
  'delivery_date': '09/05/2024', 
  'items': {
      "name": "Item 1",
      "quantity": 1,
      "price": 10.0
  },        # Added items
  'quantity': 20,           
  'status': 'Pending',       
  'quality_rating': None,     
  'acknowledgment_date': None 
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
`GET api/purchase_order/PO002/get/`
### Response:
- ```json
  {
  'vendor': vendor_id,  # Assuming self.vendor is an instance of Vendor
  'po_number': 'PO002',       
  'order_date': '09/05/2024', 
  'issue_date': '09/05/2024', 
  'delivery_date': '09/05/2024',
  'items': {
      "name": "Item 1",
      "quantity": 1,
      "price": 10.0
  },       
  'quantity': 20,             
  'status': 'Pending',       
  'quality_rating': None,     
  'acknowledgment_date': None 
  }
# Update Purchase Order (PUT)
## Parameters:
- po_id: ID of the purchase order to update.
### Example JSON Payload:
`PUT api/purchase_order/PO002/update/`
- ```json
  {
  'vendor': vendor_id,  # Assuming self.vendor is an instance of Vendor
  'po_number': 'PO002',       
  'order_date': '09/05/2024',  
  'issue_date': '09/05/2024', 
  'delivery_date': '09/05/2024',
  'items': {
      "name": "Item 1",
      "quantity": 1,
      "price": 10.0
  },       
  'quantity': 40,            
  'status': 'Pending',        
  'quality_rating': None,     
  'acknowledgment_date': None 
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

# Performance Metrics Documentation

## Introduction
This module calculates various performance metrics related to purchase orders for a given vendor.

## Class: PerformanceMetrics

### Constructor: `__init__(self, purchase_order: PurchaseOrder)`
- **Parameters:** 
  - `purchase_order`: An instance of the `PurchaseOrder` class representing the current purchase order.
- **Description:**
  - Initializes the `PerformanceMetrics` object with the given purchase order.

### Method: `calculate_on_time_delivery_rate(self)`
- **Description:**
  - Calculates the on-time delivery rate for the vendor of the current purchase order.
- **Returns:**
  - The on-time delivery rate as a percentage (rounded to 2 decimal places).
- **Logic:**
  1. Fetches all completed purchase orders for the vendor.
  2. Filters the completed orders delivered on or before the delivery date of the current purchase order.
  3. Calculates the percentage of on-time deliveries among all completed orders.

### Method: `calculate_quality_rating_average(self)`
- **Description:**
  - Calculates the average quality rating for the vendor of the current purchase order.
- **Returns:**
  - The average quality rating (rounded to 2 decimal places).
- **Logic:**
  1. Fetches all completed purchase orders for the vendor.
  2. Calculates the sum of quality ratings for all completed orders.
  3. Divides the total quality rating by the number of completed orders to obtain the average.

### Method: `calculate_average_response_time(self)`
- **Description:**
  - Calculates the average response time for the vendor of the current purchase order.
- **Returns:**
  - The average response time in seconds (rounded to 2 decimal places).
- **Logic:**
  1. Fetches all purchase orders for the vendor.
  2. Calculates the time difference between the issue date and acknowledgment date for each purchase order.
  3. Calculates the total response time and divides it by the number of purchase orders to obtain the average.

### Method: `calculate_fulfillment_rate(self)`
- **Description:**
  - Calculates the fulfillment rate for the vendor of the current purchase order.
- **Returns:**
  - The fulfillment rate as a percentage (rounded to 2 decimal places).
- **Logic:**
  1. Fetches all purchase orders for the vendor.
  2. Counts the number of successfully fulfilled orders (status 'completed' without issues).
  3. Calculates the fulfillment rate as the percentage of successful orders among all orders.

### General Logic Explanation
- The class `PerformanceMetrics` provides methods to calculate various performance metrics related to purchase orders.
- Each method fetches relevant purchase orders for the vendor of the current purchase order and performs calculations based on specific criteria.
- The logic is designed to handle scenarios like missing data points or division by zero, ensuring the robustness of the calculations.

### Code Practices
- This code follows industry-standard practices and adheres to SOLID principles.
- Dependency injection is utilized in the `PerformanceMetrics` class constructor, allowing for modular and testable code.
- The code maintains modularity and readability, contributing to its maintainability and extensibility.




  




