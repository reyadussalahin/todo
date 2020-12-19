# Todo
A simple todo webapp. This app is built to fulfill the following goals:
  - Build a simple todo webapp
  - Provide a simple rest interface to perform crud operations
  - Use google firestore as data storage
  - Deploy the app to google App Engine
  - [optional]: Administrating firebase data entities through django admin

### Tasks completed
The following tasks have been completed so far:
  - Build a simple todo webapp
  - Provide a simple rest interface to perform crud operations
  - Use google firestore as data storage
  - Deploy the app to google App Engine

### Tasks in progress(Optional)
  - [optional]: Administrating firebase data entities through django admin

The idea to solve the administration problem is create a new `Manager` for `app.models.Todo` model. As, django-admin relies upon two things to provide a way to adminitrating a db table and these are:
 1. adding model to admin
 2. and the model's underline database `Manager` which return `QuerySet` object which helps to view the data through django-admin interface.

 Now, `Manager` provides methods for updating, viewing, deleting, creating data. So, creating a new `Manager` which will talk to `Google Cloud Firestore` rather than a `SQL` database, will solve the problem.


## Web App
The web app can be easily deployed to `Google Cloud App Engine`. All the setups to deploy to app engine are already done, one just has to follow the standard procedure of deploying. And also, one may prefer to run this app locally. In such case, change your local database engine from `Google Cloud Proxy` to `Mariadb` or `MySql` database or you may also setup a `Google Cloud Sql` instance for yourself. Then, you can easily run it as you run a simple django application and also don't forget to provide `Google Cloud Firestore Credential` details, as this app uses `Google Cloud Firestore` to store `Todo` apps data.


## REST API endpoints

#### List all
```
GET /api/v1/todos/
```

```
# HTTP 200 OK
{
    "status": "success",
    "todos": [
        {
            "id": "7TbBLUgRIBfzfDpQdZJC"
            "title": "title 4",
            "description": "description 4",
            "completed": "false"
        },
        {
            "id": "C8CBCr9z3BzcocEemGpt",
            "title": "title 5",
            "description": "description 5",
            "completed": "false"
        }
    ]
}
```

#### Create a todo task
```
POST /api/v1/todos/
{
    "title": "title 7",
    "description": "description 7",
    "completed": true
}
```

```
# HTTP 201 Created
{
    "status": "success",
    "todo": {
        "id": "sc8CdnZQ5KiAstia029c"
        "title": "title 7",
        "description": "description 7",
        "completed": "true"
    }
}
```

#### Get a todo task
```
GET /api/v1/todos/sc8CdnZQ5KiAstia029c
```

```
# HTTP 200 OK
{
    "status": "success",
    "todo": {
        "id": "sc8CdnZQ5KiAstia029c"
        "title": "title 7",
        "description": "description 7",
        "completed": "true"
    }
}
```

#### Update a todo task
```
PUT /api/v1/todos/sc8CdnZQ5KiAstia029c
{
    "title": "title 7 .......",
    "description": "description 7",
    "completed": true
}
```

```
# HTTP 201 Created
{
    "status": "success",
    "todo": {
        "id": "sc8CdnZQ5KiAstia029c"
        "title": "title 7 .......",
        "description": "description 7",
        "completed": "true"
    }
}
```

#### Partial update(i.e. patch) a todo task
```
PATCH /api/v1/todos/sc8CdnZQ5KiAstia029c
{
    "description": "description 7 .......",
}
```

```
# HTTP 201 Created
{
    "status": "success",
    "todo": {
        "id": "sc8CdnZQ5KiAstia029c"
        "description": "description 7 .......",
    }
}
```

#### Delete a todo task
```
DELETE /api/v1/todos/tg3FdReE7jI2ZoPd917d
```

```
# HTTP 204 No Content
{
    "status": "success"
}
```


## LICENSE
To learn about the project license, visit [here](https://github.com/reyadussalahin/todo/blob/main/LICENSE).


## Contributing
This project is open for contributing. So, any improvements, issues or feature requests are very much welcome.
