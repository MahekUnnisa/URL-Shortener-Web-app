# URL Shortener Setup
This project is a URL shortener that allows users to shorten long URLs and track the number of clicks on the shortened link.

## Requirements
- Python 3.x
- Django 2.x
- PostgreSQL Installation(You can do an instance using https://www.railway.com)
- Clone the repository: git clone https://github.com/MahekUnnisa/URL-Shortener-Web-app.git
- Change into the project directory: cd urlshortener
- Create and activate a virtual environment:

```python3 -m venv env```

```cd env/scripts/```

```activate```

- Install the dependencies: `pip install -r requirements.txt`
- Create a new PostgreSQL database and update the settings in settings.py
- Run migrations: `python manage.py makemigrations` & `python manage.py migrate`
- Install tailwind using command `npm install package.json`
- Build tailwind using command `tailwind starts command "npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch"`
- Create a superuser: `python manage.py createsuperuser`
- Press enter to enter default details
- Run the server: `python manage.py runserver`
- Go to http://127.0.0.1:8000

### Alternate DB
SQLite3
update settings.py databas esection with
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## Usage
### Routes:
- https://127.0.0.1:8000 - Homepage
- https://127.0.0.1:8000/signup - Signup
- https://127.0.0.1:8000/login - Login
- https://127.0.0.1:8000/create - Create a new link
- https://127.0.0.1:8000/logout - Logout
- https://127.0.0.1:8000/dashboard - Dashboard to see all the links
- https://127.0.0.1:8000/linkdetails - redirected page when you create a link with details
- https://127.0.0.1:8000/admin - Admin panel of the database
- https://127.0.0.1:8000/api/create - Create a new link(API testing)

### Usage
1. Create a new link by visiting http://127.0.0.1:8000/create/
2. Use the shortened link and track clicks on it
3. View your links and click data on the dashboard http://127.0.0.1:8000/dashboard/
4. To test only apis go to https://127.0.0.1:8000/api/create

## Features
- User registration and authentication
- Shortening of URLs
- Tracking of clicks on shortened links
- Expiration of links
- can add a custom url for better management
## Future Improvements
- Adding more statistics and charts for link clicks
- Adding option for custom URLs
- Integrating with external link shortening services
- Allowing users to track clicks on multiple domains
## branches
1. master - full assignment completed before the deadline
2. other branches- working on improvements and todo
## Contributing
### Fork the repository
1. Create your feature branch: `git checkout -b new-feature`
2. Commit your changes: `git commit -am 'Add some feature'`
3. Push to the branch: `git push origin new-feature`
4. Submit a pull request
