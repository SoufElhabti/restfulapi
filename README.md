# Student Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

### List all students

**Definition**

`GET /students`

**Response**

- `200 OK` on success

```json
[
        {
            "identifier": "hatim",
            "name": "hatim",
            "Branch": "iwim",
            "Address": "paris france"
        },
        {
            "identifier": "mainteemo",
            "name": "soufiane habti",
            "Branch": "SSI",
            "Address": "tokyo japan"
        }
    ]
}
```

### Registering a new student

**Definition**

`POST /student`

**Arguments**

- `"identifier":string` 
- `"name":string` 
- `"Branch":string`
- `"Address":string` 



**Response**

- `201 Created` on success

```json
{
    "identifier": "mainteemo",
    "name": "soufiane habti",
    "Branch": "SSI",
    "Address": "tokyo japan"
}
```

## Lookup student details

`GET /student/<identifier>`

**Response**

- `404 Not Found` if the student does not exist
- `200 OK` on success


## Delete a student

**Definition**

`DELETE /student/<identifier>`

**Response**

- `404 Not Found` if the student does not exist
- `204 No Content` on success
