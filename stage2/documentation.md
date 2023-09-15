<h1>API Documentation</h1>

This documentation outlines the standard formats for requests and responses for each endpoint of the provided Flask API, along with sample usage, known limitations, and deployment instructions.

All requests should be made with the Content-Type: ```application/json header```.
Request bodies should be in ```JSON format```.

<h4>Response Format</h4>

All responses will be in ```JSON format```.
Successful responses will have a status code of 200 OK.

<strong>Endpoints</strong>
1. Create a Person Record
Endpoint: ```POST /api/person```

Request Body:

    json

    {
        "name": "string",
        "age": integer
    }

Response:

    json

        {
            "id": integer,
            "name": "string",
            "age": integer
        }

2. <strong>Get All Persons</strong>
Endpoint: ```GET /api/person```

Response:
    json

    [
        {
            "id": integer,
            "name": "string",
            "age": integer
        },
        ...
    ]

3. <Strong>Get Person by ID<strong>

Endpoint: ```GET /api/person/{id}```

Response:

    json

    {
        "id": integer,
        "name": "string",
        "age": integer
    }

<strong>Error Response (Person Not Found):</strong>

    json

        {
            "message": "Person not found"
        }

4. <strong>Get Person by Name</strong>

Endpoint: ```GET /api/person/{name}```

Response:

    json

        {
            "id": integer,
            "name": "string",
            "age": integer
        }

Error Response (Person Not Found):

    json

        {
            "message": "Person not found"
        }

5. <strong>Update Person by ID</strong>

Endpoint: ```PUT /api/person/{id}```
Request Body:

    json

    {
        "name": "string",
        "age": integer
    }

Response:

    json

    {
        "id": integer,
        "name": "string",
        "age": integer
    }

Error Response (Person Not Found):

    json

        {
            "message": "Person not found"
        }

6. <strong>Update Person by Name</strong>

Endpoint: ```PUT /api/person/{name}```
Request Body:

    json

        {
            "name": "string",
            "age": integer
        }

Response:

    json

        {
            "id": integer,
            "name": "string",
            "age": integer
        }

Error Response (Person Not Found):

    json

        {
            "message": "Person not found"
        }

7. <strong>Delete Person by ID</strong>

Endpoint: ```DELETE /api/person/{id}```
Response:

    json

        {
            "id": integer,
            "name": "string",
            "age": integer
    }

Error Response (Person Not Found):

json

    {
        "message": "Person not found"
    }

<h3>Sample Usage</h3>
1. <strong>Creating a Person Record</strong>
Request:

    http

    POST /api/person
    Content-Type: application/json

    {
        "name": "John Doe",
        "age": 30
    }

Response (Success):

    json

    {
        "id": 1,
        "name": "John Doe",
        "age": 30
    }

2. Getting All Persons

Request:

    http

    GET /api/person

Response (Success):

    json

    [
        {
            "id": 1,
            "name": "John Doe",
            "age": 30
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "age": 25
        },
        ...
    ]

3. Getting a Person by ID

Request:

    http

    GET /api/person/1

Response (Success):

    json

    {
        "id": 1,
        "name": "John Doe",
        "age": 30
    }

Response (Person Not Found):

    json

    {
        "message": "Person not found"
    }

<h2>Known Limitations</h2>

The API uses SQLite as the database, which is suitable for development and testing but may not be ideal for production use. Consider using a more robust database system for production.

Error handling in this code is minimal and can be improved for production use. Additional error codes and meaningful error messages can be implemented.

<h2><Strong>Deployment Instructions</strong></h2>

To deploy the API locally, follow the setup and run instructions provided in the README.md file. The API will be accessible at ```http://localhost:9000```.

For deploying the API on a server in a production environment, additional steps and configurations are required. These include setting up a web server (e.g., Nginx) and using a production-ready database system (e.g., PostgreSQL or MySQL). Ensure proper security measures are taken when deploying in a production environment.

You can use the provided README.md and documentation.md as templates and adjust them according to your specific needs and preferences.
