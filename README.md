# API Documentation

Here is a list of available endpoints for the API:

| Endpoint                                 | Description                                           |
|------------------------------------------|-------------------------------------------------------|
| '`admin/`'                               | Admin panel                                           |
| '`swagger/`'                             | Swagger  Document API endpoints, including parameters, request bodies, and response schemas.|
| '`redoc/`'                               | Redoc  Document API endpoints, including parameters, request bodies, and response schemas.|
| '`api/v1/register/`'                    | Register a new user                                   |
| '`api/v1/login/`'                       | User login                                            |
| '`api/v1/logout/`'                      | User logout                                           |
| '`api/v1/users/`'                       | List all users                                        |
| '`api/v1/users/profile/`'               | Retrieve authenticated user profile                   |
| '`api/v1/users/<uuid:pk>/update/`'           | Retrieve user detail by slug                          |
| '`api/v1/users/<uuid:pk>/`'           | Update user detail by slug                            |
| '`api/v1/product/`'                     | List all products                                     |
| '`api/v1/product/create/`'              | Create a new product                                  |
| '`api/v1/product/update/<uuid>/`'         | Update an existing product (identified by its primary key) |
| '`api/v1/product/delete/<uuid>/`'         | Delete an existing product (identified by its primary key)|
| '`api/v1/establishment/`'               | List all establishments                               |
| '`api/v1/establishment/create/`'        | Create a new establishment                            |
| '`api/v1/establishment/update/<uuid:pk>/`' | Update an existing establishment (identified by its UUID)|
| '`api/v1/establishment/delete/<uuid:pk>/`' | Delete an existing establishment (identified by its UUID)|


<br>
<br>


For more detailed information, refer to the API documentation.

# Reviro

This project is a simple product inventory management system. It allows users to add,
update, delete, and view information about establishments and products in the inventory.<br>

## _Update_ 


All views.py files are collected in this directory. <br>

Also, inside api/, create two directories auth/ and v1/. <br>

auth/ - in any case, I always handle my own authentication (for example, token-based), as well as various permissions for API endpoints, etc. <br>

v1/ - API version, in the future it can be changed to v2.0, v3.0, etc. Here directories (python packages, identical to the application names in <br>apps) are collected, inside which views.py files are already located."<br>




Introduced **<u>fixtures</u>** to provide stable environments for automated _testing_. <br>
Implemented **<u>logging</u>** functionality to track actions and errors, enhancing debugging capabilities and process monitoring. <br>
Included a **<u>Postman collection</u>** for streamlined API testing, enabling efficient verification of endpoint functionality. <br>
Enhanced security features with **<u>authentication</u>** and **<u>authorization</u>** mechanisms, **<u>including roles</u>** and **<u>permissions</u>**. <br>
Established full **<u>CRUD</u>** (Create, Read, Update, Delete) operations for managers, ensuring comprehensive control over resources. <br>
Enabled users with viewing, **<u>searching_**, and **<u>filtering</u>** capabilities, restricting other CRUD operations for enhanced data security.<br>

## Getting Started

Follow these steps to get the project up and running:

1. ### Clone the repository:<br>
``` bash 
git clone https://github.com/Kylych-dev/reviro_test.git
``` 
<br>

``` bash 
cd reviro_test
```

2. ### Build and run containers using Docker Compose: <br>

Start containers in the foreground and build images.<br>

``` bash 
docker-compose up --build
``` 
<br>

Start containers in the background. <br>


``` bash 
docker-compose up -d
``` 
<br>
    
Create database migrations. <br>

``` bash 
docker exec -it my_container sh -c 'python3 manage.py makemigrations'
``` 
<br>
    
    Apply migrations to create the database schema.<br>

``` bash 
docker exec -it my_container sh -c "python3 manage.py migrate"
``` 
<br>
    
Stop and remove containers, networks, and volumes.<br>

``` bash 
docker compose down 
``` 
<br>


3. ### Access Swagger documentation:

    Open your browser and navigate to the following URL: <br>
```
    http://0.0.0.0:8000/swagger/
``` 
<br>
    Here you will find documentation for all available API endpoints, including parameters, request bodies, and response schemas.<br>

4. ### Using the API

    You can use any HTTP client, such as curl or Postman, to send requests to the API. Below are examples of requests and expected responses: <br>
    Get a list of establishments (GET /establishments/): <br>

```
    curl -X GET http://localhost:8000/establishments/
``` 
<br>
    
#### Response:
```
    [
        {
            "name": "Example Establishment",
            "description": "Description of the establishment",
            "locations": "Location 1, Location 2",
            "opening_hours": "9:00 AM - 5:00 PM",
            "requirements": "Requirements for the establishment"
        },
        {
            "name": "Another Establishment",
            "description": "Another description",
            "locations": "Location 3, Location 4",
            "opening_hours": "8:00 AM - 6:00 PM",
            "requirements": "Other requirements"
        }
    ]
```

4. Add a new establishment (POST /establishments/): <br>
```
    curl -X POST -H "Content-Type: application/json" -d '{"name": "New Establishment", "description": "Description of the new establishment", "locations": "New Location", "opening_hours": "8:30 AM - 4:30 PM", "requirements": "New requirements"}' http://localhost:8000/establishments/
```

#### Response:
```
    {
        "name": "New Establishment",
        "description": "Description of the new establishment",
        "locations": "New Location",
        "opening_hours": "8:30 AM - 4:30 PM",
        "requirements": "New requirements"
    }
```



5. ### Stopping Containers: <br>

``` bash 
    docker-compose down
```


## Running Tests

Follow these steps to run the tests:

Activate Virtual Environment (if applicable):

If you are using a virtual environment, activate it:

 
``` bash 
source venv/bin/activate 
```

Navigate to Project Directory:

Change your current directory to the project directory:


``` bash
cd /Desktop/practice/reviro_test/backend
```

### Run Tests:

Execute the following command to run the tests:

``` bash 
pytest
```


## Applying Fixtures

Install Dependencies:
 
``` bash 
pip install -r requirements.txt
```

Load Fixtures:

``` bash
./manage loaddata fixtures main.json
```

### Run Tests:

Execute the following command to run the tests:

``` bash 
pytest
```



## Contributing

`telegram: _@mirbekov0909_` <br>
<br>

`email: tteest624@gmail.com` <br>
<br>

`email: mirbekov1kylych@gmail.com`



