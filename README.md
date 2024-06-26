# Python version `3.12.3` is used in this project. 
# Please see the instructions below to setup the project in your computer.

## Steps:- 
## 1) Download the Repo and extract the repo
## 2) Navigate to the vendormanage-master folder (It should have manage.py file in it "just to identify you are in the right folder)
## 3) Open the terminal in the same folder.
## 4) Setup a virtual environment by running the commands given below in your terminal.
     `pip install virtualenv`
     `virtualenv YourEnviromentName`
     `YourEnvironmentName\scripts\activate` activate you environment
## 5) Once you have created and activated your environment run this command.
     `pip install -r requirements.txt` it installs all of the necessary dependencies for running this project
## 6) After Installing run the following commands in sequence
     `python manage.py makemigrations`
     `python manage.py migrate`
     `python manage.py runserver`
## 7) To run the Test suite use the command givin below (Test suite commands do not run when the Django server is running. Stop the server with CTRL + C)
     `python manage.py test`
## 8) To run the test suite for a specific app run the commands below
     `python manage.py test purchase_order.tests`
     `python manage.py test vendor.tests`
     
# Please, navigate to these folders `[purchase_order, vendor]` to see the documentation and working of Each API endpoint.

   
## `All of the endpoints are restricted and requires an authentication Token to be accessed.`

# Steps for registering yourself and obtaining access token (Use Postman to interact with APIs. download Postman here [Download Postman](https://www.postman.com/downloads/):-
## User Registration

- **Path:** `api/authapp/user/register/`
- **Method:** POST
- **Description:** This endpoint is used to register a new user by providing a username and password in JSON format.
- **Input:** JSON object containing `username` and `password`.
- **Returns:** Upon successful registration, it returns a response with user details. If registration fails, it returns an error message.
- **Usage:** Send a POST request to `/user/register/` with the following JSON data in the request body:
  ```json
  {
    "username": "example_user",
    "password": "example_password"
  }
  

## Authentication Token Obtainment

- **Path:** `api/authapp/token/`
- **Method:** POST
- **Description:** This endpoint is used to obtain a JSON Web Token (JWT) for user authentication.
- **Input:** JSON object containing `username` and `password`.
- **Returns:** Upon successful authentication, it returns a response with a JWT. If authentication fails, it returns an error message.
- **Usage:** Send a POST request to `/token/` with the user credentials in the request body.
  ```json
  {
    "username": "example_user",
    "password": "example_password"
  }
 ### see the image
  ![Alt text](https://github.com/jatin-c/vendormanage/blob/master/images/Screenshot%20(52).png)

## Adding the token to the bearer section in postman. 
 - Navitage to Authorization section
 - change the auth type to bearer token
 - Paste the obtained token in Token input area
### see the image
  ![Alt text](https://github.com/jatin-c/vendormanage/blob/master/images/Screenshot%20(53).png)
  

## Authentication Token Refreshment

- **Path:** `api/authapp/token/refresh/`
- **Method:** POST
- **Description:** This endpoint is used to refresh an existing JWT token.
- Input: JSON object containing refresh token.
- **Returns:** Upon successful token refreshment, it returns a response with a new JWT. If refreshment fails, it returns an error message.
- **Usage:** Send a POST request to `/token/refresh/` with a valid refresh token in the request body.
- ```json
  {
    "refresh": "valid_refresh_token"
  }

# Note :- Its necessary to obtain the token and paste it in the bearer section without it you won't be able to access any of the endpoint and will see this error.
- ```json
  {
    "detail": "Authentication credentials were not provided."
  }


# Refer to this concise list of URLs

## Authentication
- **User Registration:**
  - POST: `http://127.0.0.1:8000/api/authapp/user/register/`

- **Get Token:**
  - POST: `http://127.0.0.1:8000/api/authapp/token/`

- **Refresh Token:**
  - POST: `http://127.0.0.1:8000/api/authapp/token/refresh/`

## Vendor
- **List Vendors:**
  - GET: `http://127.0.0.1:8000/api/vendor/`
  
- **Retrieve Vendor:**
  - GET: `http://127.0.0.1:8000/api/vendor/<vendor_id>/`

- **Create Vendor:**
  - POST: `http://127.0.0.1:8000/api/vendor/create/`

- **Update Vendor:**
  - PUT: `http://127.0.0.1:8000/api/vendor/<vendor_id>/update/`

- **Delete Vendor:**
  - DELETE: `http://127.0.0.1:8000/api/vendor/<vendor_id>/delete/`

- **Vendor Performance:**
  - GET: `http://127.0.0.1:8000/api/vendor/<vendor_id>/performance/`

- **Vendor Performance History:**
  - GET: `http://127.0.0.1:8000/api/vendor/<vendor_id>/performancehistory/`

## Purchase Order
- **List All Purchase Orders:**
  - GET: `http://127.0.0.1:8000/api/purchase_order/listall/`
- **List All Purchase Orders filtered by Vendor:**
  - GET: `http://127.0.0.1:8000/api/purchase_order/listall/?vendor=vendor_id`
  
- **Create Purchase Order:**
  - POST: `http://127.0.0.1:8000/api/purchase_order/create/`

- **Retrieve Purchase Order:**
  - GET: `http://127.0.0.1:8000/api/purchase_order/<po_id>/get/`

- **Update Purchase Order:**
  - PUT: `http://127.0.0.1:8000/api/purchase_order/<po_id>/update/`

- **Delete Purchase Order:**
  - DELETE: `http://127.0.0.1:8000/api/purchase_order/<po_id>/delete/`

- **Acknowledge Purchase Order:**
  - PUT: `http://127.0.0.1:8000/api/purchase_order/<po_id>/acknowledge/`

## Historical Performance
- **List All Historical Performances:**
  - GET: `http://127.0.0.1:8000/api/vendor/historicalperformance/listall/`
