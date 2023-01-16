# Data-Scraper (Python+Django, Vue3+Vuetify)
<hr />

### This application retrieves information from  [Microsoft store](https://apps.microsoft.com/store/category/Business) and return it in convenient way.
> ### Technologies used:
>
> - Docker & Docker-Compose
> - Celery
> - Redis
> - Django Rest Framework
> - **Selenium**
> - Vuetify 3
<hr />
## Instalation

### 1. Start application
```bash
docker-compose up --build
```

### 2. Make database migrations
```bash
docker-compose exec webapp bash
``` 
```bash
cd src/
``` 
```bash
python manage.py makemigrations
``` 
```bash
python manage.py migrate
``` 

## 3. Run UI application
```bash
cd linguanex_ui/
```
```bash
npm install
```
```bash
npm run serve
```
<hr />

## Result 
[<img style="witdh:100px" src="https://res.cloudinary.com/djd9bqakh/image/upload/v1673859333/screanshot_vr0n9v.png">](https://res.cloudinary.com/djd9bqakh/image/upload/v1673859333/screanshot_vr0n9v.png)





