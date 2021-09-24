# tickets
_ticket-system API **tutorial model**_

## Run

```
uwsgi --socket 127.0.0.1:5000 --protocol=http -w wsgi:app
```

## API Docs

| Method | Endpoint | Data | For what |
| --- | --- | --- | --- |
| GET | /tickets/ticket/{id} | id - ticket_id | Get ticket |
| POST | /tickets/ticket | title, body, email - required fields | Create ticket |
| POST | /tickets/comment/{id} | id - ticket_id; comment, email  - required fields | Add comment for ticket |
| PUT | /tickets/ticket/{id} | id - ticket_id, status - required field | Change ticket status |

## Responses

#### Get ticket
```json
{
  "body": "string", 
  "change_datetime": "string", 
  "comments": [
    {
      "comment": "string", 
      "comment_id": 0, 
      "create_datetime": "string", 
      "email": "string"
    }
  ], 
  "create_datetime": "string", 
  "email": "string", 
  "status": "string", 
  "ticket_id": 0, 
  "title": "string"
}
```

#### Create ticket
```json
{
  "body": "string", 
  "email": "string", 
  "ticket_id": 0, 
  "title": "string"
}
```

#### Add comment for ticket
```json
{
  "comment": "string", 
  "comment_id": 0, 
  "create_datetime": "string", 
  "email": "string", 
  "ticket_id": 0
}
```

#### Change ticket status
```json
{
  "status": "string", 
  "ticket_id": 0
}
```

## Technologies

* Flask for API constructor
* Redis for Cache
* PostgresSQL for database
* SQLAlchemy for ORM
* uWSGI for Web-server (instead of Werkzeug)