# Hosted API Usage Guide

This API provides CRUD (Create, Read, Update, Delete) operations for managing a list of persons' biodata. You can interact with the API by making HTTP requests to the provided endpoints.

API Base URL: http://16.171.139.244/api/person

## Endpoints

### 1. Create a Person Record (POST)
Create a new person record with a name and age.

- **Endpoint:** `/api/person`
- **Method:** POST
- **Request Body:**

    ```json
    {
        "name": "string",
        "age": integer
    }
    ```

- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

### 2. Get All Persons (GET)
Retrieve a list of all persons' biodata.

- **Endpoint:** `/api/person`
- **Method:** GET
- **Response:**

    ```json
    [
        {
            "id": integer,
            "name": "string",
            "age": integer
        },
        ...
    ]
    ```

### 3. Get Person by ID (GET)
Retrieve a person's biodata by their ID.

- **Endpoint:** `/api/person/{id}`
- **Method:** GET
- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

- **Error Response (Person Not Found):**

    ```json
    {
        "message": "Person not found"
    }
    ```

### 4. Get Person by Name (GET)
Retrieve a person's biodata by their name.

- **Endpoint:** `/api/person/{name}`
- **Method:** GET
- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

- **Error Response (Person Not Found):**

    ```json
    {
        "message": "Person not found"
    }
    ```

### 5. Update Person by ID (PUT)
Update a person's biodata by their ID.

- **Endpoint:** `/api/person/{id}`
- **Method:** PUT
- **Request Body:**

    ```json
    {
        "name": "string",
        "age": integer
    }
    ```

- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

- **Error Response (Person Not Found):**

    ```json
    {
        "message": "Person not found"
    }
    ```

### 6. Update Person by Name (PUT)
Update a person's biodata by their name.

- **Endpoint:** `/api/person/{name}`
- **Method:** PUT
- **Request Body:**

    ```json
    {
        "name": "string",
        "age": integer
    }
    ```

- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

- **Error Response (Person Not Found):**

    ```json
    {
        "message": "Person not found"
    }
    ```

### 7. Delete Person by ID (DELETE)
Delete a person's biodata by their ID.

- **Endpoint:** `/api/person/{id}`
- **Method:** DELETE
- **Response:**

    ```json
    {
        "id": integer,
        "name": "string",
        "age": integer
    }
    ```

- **Error Response (Person Not Found):**

    ```json
    {
        "message": "Person not found"
    }
    ```

## Sample Usage

1. Creating a Person Record

   Request:

   ```http
   POST http://16.171.139.244/api/person
   Content-Type: application/json

   {
       "name": "John Doe",
       "age": 30
   }
    ```
2. Getting a Person Record

   Request:

   ```http
   GET http://16.171.139.244/api/person
   ```
   Response Success:

   [
    ```{
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

### Important Note

The API is hosted at ```http://16.171.139.244/api/person```

Feel free to use the provided API endpoints to manage persons' biodata as needed. Adjust the sample requests and responses to suit your requirements.
