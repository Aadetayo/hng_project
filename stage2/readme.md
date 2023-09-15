<h1>Setup, Run, and Use the API</h1>

This README provides instructions on how to set up, run, and use the API implemented in the provided Python code.
Setup

Clone the Repository: Begin by cloning this repository to your local machine using the following command:

    bash

    git clone <repository-url>

Install Dependencies: Navigate to the project directory and install the required dependencies using pip:

    bash

    pip install flask flask_sqlalchemy flask_marshmallow

<h2>Run</h2>
Database Initialization: Before running the API, you need to initialize the SQLite database. Run the following command to create the database:


    bash

    python
    
python

    from app import db
    with app.app_context():
        db.create_all()

Run the API: Start the Flask development server to run the API locally:

    bash

    python app.py

The API should now be running at ```http://localhost:9000```.

<h2>Use the API</h2>

The API exposes several endpoints for CRUD (Create, Read, Update, Delete) operations on person records. You can interact with the API using tools like curl, Postman, or by writing your own code.
Endpoints:

Create a Person Record:

    http

    POST /api/person

Example Request:

    json

    {
        "name": "John Doe",
        "age": 30
    }

Get All Persons:

    http

    GET /api/person

Get Person by ID:

    http

    GET /api/person/{id}

Get Person by Name:

    http

    GET /api/person/{name}

Update Person by ID:

    http

    PUT /api/person/{id}

Example Request:

    json

    {
        "name": "Updated Name",
        "age": 35
    }

Update Person by Name:

    http

    PUT /api/person/{name}

Example Request:

    json

    {
        "name": "Updated Name",
        "age": 35
    }

Delete Person by ID:

    http

    DELETE /api/person/{id}

Sample Usage:

1. To create a new person record, make a POST request to ```/api/person``` with the person's name and age in the request body.
2. To retrieve all person records, make a GET request to ```/api/person```.
3. To update a person's information by their ID, make a PUT request to ```/api/person/{id}``` with the updated data in the request body.

To delete a person record by their ID, make a DELETE request to ```/api/person/{id}```.


<h2><strong>Known Limitations </strong></h2>

This API uses SQLite as the database, which is suitable for development and testing purposes. For production, consider using a more robust database system like PostgreSQL or MySQL.

Error handling is minimal in this code and can be improved for production use.

Local Deployment

To deploy the API locally, follow the setup and run instructions provided earlier. The API will be accessible at ```http://localhost:9000```.

For deploying the API on a server, additional steps and configurations are required, such as setting up a web server (e.g., Nginx) and using a production-ready database. Ensure proper security measures are taken when deploying in a production environment.
