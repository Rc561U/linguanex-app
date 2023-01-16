# Scraper (Python, Django, Vue3)

### Start application
```bash
docker compose up --build
```

### Make database migrations
```bash
docker compose exec webapp bash
``` 
```bash
cd src/
``` 
```bash
python manage.py migrate
``` 

## Run UI application
```bash
cd linguanex_ui/
```
```bash
npm install
```
```bash
npm run serve
```





