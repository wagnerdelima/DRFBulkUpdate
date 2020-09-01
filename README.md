Please create a docker postgres container with:

```
docker run --name postgres -p 5555:5432 -e POSTGRES_PASSWORD=0119 -e POSTGRES_DB=drf -d postgres
```

Ir order to run the test:
```
pytest
```
