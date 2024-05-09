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


  




