# Your Progress
## Start tracking your progress!
We created this project to help you with your productivity.
This tool helps you track all your activities like sports, work, hobbies

## How to use
- Sign up
- Create first project
- Start to commit your activities
- See your progress

![](https://github.com/ZanMax/your-progress/raw/main/static/img/screenshot01.png)

## Configuration
create .env file in enlearn directory
```
SECRET_KEY=<generate_secret_key>
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=<db_host>
DB_PORT=<db_port>
TIMEZONE=America/Vancouver
```

## Deployment
### Build
```
docker build -t 10.0.0.200:5000/progress:0.0.1-arm .
```
### Push
```
docker push 10.0.0.200:5000/progress:0.0.1-arm
```
### Deploy
```
kubectl -n dev apply -f .
```