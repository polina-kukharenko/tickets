Run

```
uwsgi --socket 127.0.0.1:5000 --protocol=http -w wsgi:app
```