# tickets
_ticket-system API **tutorial model**_

## Run

```
python3 main.py
```

## API Docs

| Method | Endpoint | Data | For what |
| --- | --- | --- | --- |
| GET | /tickets/{id} | id - ticket_id | Get ticket |
| POST | /tickets/create | title, body, email - required fields | Create ticket |
| POST | /tickets/{id}/comment | id - ticket_id; comment, email  - required fields | Add comment for ticket |
| PUT | /tickets/{id} | id - ticket_id, status - required field | Change ticket status |

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
