# Catalog system for products

## Prerequisites
```commandline
python 3.9+
pip-tools 6.12.1+
make
docker
docker-compose
```

Create new file `.envs/.development` based on example
```commandline
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=
DATABASE_URL=
```

## Installation via docker
Create new file `.envs/.db` based on example
```commandline
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

And run
```commandline
make up
```

## Installation via console
```commandline
pip install pip-tools
make install
```

Run the following commands
```commandline
python manage.py makemigrations
python manage.py runserver
```

To create super user run the following command
```commandline
python manage.py createsuperuser
```

## Mentions
This command will help you to update requirements, run tests and lints
```commandline
make help
```

## API documentation
Admin panel
```commandline
curl http://{host}/admin/
```

### Swagger API
```commandline
curl http://{host}/docs/
```

### API that word without authentication
```commandline
curl http://{host}/catalog/
curl http://{host}/catalog/{product_id}
```

### API that requires authentication

Example product json
```json
{
    "sku": "test_sku",
    "name": "test_name",
    "price": 100,
    "brand": "test_brand"
}
```

Create product
```commandline
curl -d "{product_json}" -X POST http://{host}/catalog
```

Delete product
```commandline
curl -X DELETE http://{host}/catalog/{product_id}
```

Update product
```commandline
curl -d "{product_json}" -X PUT http://{host}/catalog/{product_id}
```