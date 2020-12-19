# Todo
A simple todo webapp. This app is built to fulfill the following goals:
  - Build a simple todo webapp
  - Provide a simple rest interface to perform crud operations
  - Use google firestore as data storage
  - Deploy the app to google App Engine
  - [optional]: Administrating firebase data entities through django admin

### Tasks completed
The following tasks have been completed so far:
  - Provide a simple rest interface to perform crud operations
  - Use google firestore as data storage
  - Deploy the app to google App Engine

### Tasks on progress
  - Simple webapp UI for the app
  - [optional]: Administrating firebase data entities through django admin


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
PUT /api/v1/todos/sc8CdnZQ5KiAstia029c
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
