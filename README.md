# Catalog system for products

Projects run sqlite, so you do not need to set up any db. 
Also, there is no .env file for faster start.


## Prerequisites
```commandline
python 3.9+
pip-tools 6.12.1+
make
```

## Installation
```commandline
pip install pip-tools
make install
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

### Open API
```commandline
curl http://{host}/catalog/openapi
```

### API that word without authentication
```commandline
curl http://{host}/catalog/
curl http://{host}/catalog/{product_id}
```

### API that requires authentication

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