
# Opi Analytics Map
## Run project

Please, before running the project:

 1. Rename the file *backend/secret_example.py* to *secret.py*.
 2. Get an **API KEY** from https://developer.mapquest.com/ and set it in the file *frontend/src/Utils/Popup.js* in line 3.
 3. Consider adding, removing or updating data from the file *backend/locations-sample.csv* in order to get different results (the file contains 500 registers).
 4. You must have **Docker** and **Docker Compose** installed
 5. Go the root folder of this project and run the next comand (wait until services are up).

```bash
$ docker-compose up
```
## Infrastructure
### Enviroment
 - Docker
 - Docker Compose
### Backend
 - Django 3.1.1
 - Python 3.7
 - MySQL 5.7 (GIS)
 
### Frontend
 - React 17.0.1
 - Leaflet 1.7.1

### Services
 - MapQuest
