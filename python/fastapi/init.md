```
pip install -r reqs.txt
```

```
alembic init alembic
```

Apply migrations:

```
alembic upgrade head
``` 

New migration:

```
alembic revision --autogenerate -m "$message"
```
