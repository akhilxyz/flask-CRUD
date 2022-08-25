#!/bin/bash

echo -e "\n>> Clearing Chache Mermory"
find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf

docker-compose down
echo -e "\n>> Building applications and databases"

docker-compose build

echo -e "\n>> Starting applications and databases"
docker-compose up -d

echo -e "\n>> All services are up
 * Running on http://127.0.0.1:5000
 * Running on http://172.27.0.2:5000
"

