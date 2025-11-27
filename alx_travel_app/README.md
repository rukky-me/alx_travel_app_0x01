This task guides learners through creating essential backend components in Django by defining database models, setting up serializers for API data representation, and implementing a management command to seed the database

For this task the alx_travel_app is duplicated into alx_travel_app_0x00


To duplicate alx_travel_app into alx_travel_app_0x00
The following was done:
git clone the new repo alx_travel_app_0x00

cd ~ to go the home directory where both repositories/directories are resident.

Create the folder structure in alx_travel_app_0x00 using "mkdir -p alx_travel_app_0x00/alx_travel_app"

Next copy alx_travel_app into alx_travel_app_0x00 using "cp -r alx_travel_app/alx_travel_app/alx_travel_app/* alx_travel_app_0x00/alx_travel_app/"

#########
Next the project is duplicated into alx_travel_app_0x01 with the below Objective

>>>>API Development for Listings and Bookings in DjangoBuild API views to manage listings and bookings, and ensure the endpoints are documented with Swagger.

Instructions

Duplicate Project:

Duplicate the project alx_travel_app_0x00 to alx_travel_app_0x01
Create ViewSets:

In listings/views.py, create viewsets for Listing and Booking using Django REST framework’s ModelViewSet.
Ensure that these views provide CRUD operations for both models.
Configure URLs:

Use a router to configure URLs for the API endpoints.
Ensure endpoints follow RESTful conventions and are accessible under /api/.
Test Endpoints:

Test each endpoint (GET, POST, PUT, DELETE) using a tool like Postman to ensure they work as expected.