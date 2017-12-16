# service-fusion

> demo for service fusion interview project

> you must have docker installed to run the project locally

## Build With Docker

``` bash

# in this directory
docker-compose build

# then run the docker-compose
docker-compose up -d

```


``` bash

# in your /etc/hosts file add the line
0.0.0.0 any.jawn.it

if you encounter an error when you first fire up the app, you may need to sync your newly created database:
docker exec -it servicefusion_api_1 ./manage.py migrate

```
Point your browser to http://any.jawn.it

Enjoy!
