# VendorListAPIView

### Description:
This API endpoint allows authenticated users to List all vendors vendor.

### Endpoint:
- **URL:** `/api/vendor/`
- **Request Type:** GET

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

# VendorCreateAPIView
### Description:
This API endpoint allows authenticated users to create a new vendor.

### Endpoint:
- **URL:** `/api/vendors/create/`
- **Request Type:** POST

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.
  
#### Example JSON Payload:
- ```json
  {
    "name": "Example Vendor",
    "contact_details": "John Doe",
    "address": "123 Main St, Anytown",
    "vendor_code": "VENDOR123",
    "on_time_delivery_rate": 95.5,
    "quality_rating_average": 4.2,
    "average_response_time": 2.5,
    "fulfillment_rate": 98.7
  }

# Response:
Success Response (201):
Content: { "message": "Vendor created successfully" }
Description: Indicates that the vendor was successfully created.
Error Response (400):
Content: Error details specifying which fields failed validation.
Description: Indicates that there was an error in the data provided. The response will contain details about the validation errors.

## VendorRetrieveAPIView

### Description:
This API endpoint allows authenticated users to retrieve details of a specific vendor.

### Endpoint:
- **URL:** `/api/vendor/<vendor_id>/`
- **Request Type:** GET

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### URL Parameters:
- `vendor_id` (integer, required): The unique identifier of the vendor to retrieve.

### Response:
- **Success Response (200):**
  - **Content:** JSON data containing details of the vendor.
  - **Example:** 
    ```json
    {
      "id": 1,
      "name": "Example Vendor",
      "contact_details": "John Doe",
      "address": "123 Main St, Anytown",
      "vendor_code": "VENDOR123",
      "on_time_delivery_rate": 95.5,
      "quality_rating_average": 4.2,
      "average_response_time": 2.5,
      "fulfillment_rate": 98.7
    }
    ```
  - **Description:** Returns details of the specified vendor.
- **Error Response (404):**
  - **Content:** `{ "detail": "Vendor does not exist" }`
  - **Description:** Indicates that the vendor with the provided `vendor_id` does not exist.

## VendorUpdateAPIView

### Description:
This API endpoint allows authenticated users to update details of a specific vendor.

### Endpoint:
- **URL:** `/api/vendor/<vendor_id>/update/`
- **Request Type:** PUT

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### URL Parameters:
- `vendor_id` (integer, required): The unique identifier of the vendor to update.

### Input:
- The request body should contain JSON data with the fields to be updated.
  - Fields can be partially updated.
  - Fields not included in the request body remain unchanged.

#### Example JSON Payload:
- ```json
  {
    "name": "Updated Vendor Name",
    "contact_details": "New Contact Details",
    "address": "New Address",
    "on_time_delivery_rate": 98.5
  }
### Error Response (404):
Content: { "detail": "Vendor does not exist" }
Description: Indicates that the vendor with the provided vendor_id does not exist.

## VendorDeleteAPIView

### Description:
This API endpoint allows authenticated users to delete a specific vendor.

### Endpoint:
- **URL:** `/api/vendor/<vendor_id>/delete/`
- **Request Type:** DELETE

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### URL Parameters:
- `vendor_id` (integer, required): The unique identifier of the vendor to delete.

### Response:
- **Success Response (204):**
  - **Content:** No content.
  - **Description:** Indicates that the vendor was successfully deleted.
- **Error Response (404):**
  - **Content:** `{ "detail": "Non-existing vendor cannot be deleted" }`
  - **Description:** Indicates that the vendor with the provided `vendor_id` does not exist.

## VendorPerformanceAPIView

### Description:
This API endpoint allows authenticated users to retrieve performance metrics of a specific vendor.

### Endpoint:
- **URL:** `/api/vendor/<vendor_id>/performance/`
- **Request Type:** GET

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### URL Parameters:
- `vendor_id` (integer, required): The unique identifier of the vendor.

### Response:
- **Success Response (200):**
  - **Content:** JSON data containing performance metrics of the vendor.
  - **Example:** 
    ```json
    {
      "on_time_delivery_rate": 95.5,
      "quality_rating_avg": 4.2,
      "average_response_time": 2.5,
      "fulfillment_rate": 98.7
    }
    ```
  - **Description:** Returns the performance metrics of the specified vendor.
- **Error Response (404):**
  - **Content:** `{ "error": "Vendor not found" }`
  - **Description:** Indicates that the vendor with the provided `vendor_id` does not exist.
 
## VendorPerformanceHistoryAPIView

### Description:
This API endpoint allows authenticated users to retrieve historical performance data of a specific vendor.

### Endpoint:
- **URL:** `/api/vendor/<vendor_id>/performancehistory/`
- **Request Type:** GET

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### URL Parameters:
- `vendor_id` (integer, required): The unique identifier of the vendor.

### Response:
- **Success Response (200):**
  - **Content:** JSON data containing historical performance data of the vendor.
  - **Example:** 
    ```json
    [
      {
        "id": 1,
        "vendor_id": 1,
        "performance_date": "2022-05-01",
        "on_time_delivery_rate": 95.5,
        "quality_rating_avg": 4.2,
        "average_response_time": 2.5,
        "fulfillment_rate": 98.7
      },
      {
        "id": 2,
        "vendor_id": 1,
        "performance_date": "2022-06-01",
        "on_time_delivery_rate": 96.2,
        "quality_rating_avg": 4.3,
        "average_response_time": 2.7,
        "fulfillment_rate": 99.0
      }
    ]
    ```
  - **Description:** Returns the historical performance data of the specified vendor.
- **Error Response (404):**
  - **Content:** `{ "error": "No historical performance data found for the vendor" }`
  - **Description:** Indicates that there is no historical performance data available for the specified vendor.
 
## HistoricalPerformanceListAPIView

### Description:
This API endpoint allows authenticated users to retrieve a list of all historical performance entries.

### Endpoint:
- **URL:** `/api/vendor/historicalperformance/listall/`
- **Request Type:** GET

### Authentication:
- Requires authentication. Users must provide a valid token in the request headers.

### Response:
- **Success Response (200):**
  - **Content:** JSON data containing a list of all historical performance entries.
  - **Example:** 
    ```json
    [
      {
        "id": 1,
        "vendor_id": 1,
        "performance_date": "2022-05-01",
        "on_time_delivery_rate": 95.5,
        "quality_rating_avg": 4.2,
        "average_response_time": 2.5,
        "fulfillment_rate": 98.7
      },
      {
        "id": 2,
        "vendor_id": 2,
        "performance_date": "2022-06-01",
        "on_time_delivery_rate": 96.2,
        "quality_rating_avg": 4.3,
        "average_response_time": 2.7,
        "fulfillment_rate": 99.0
      }
    ]
    ```
  - **Description:** Returns a list of all historical performance entries.




 




  
