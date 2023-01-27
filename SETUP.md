# URL Shortener Setup
This project is a URL shortener that allows users to shorten long URLs and track the number of clicks on the shortened link.

## Requirements
- Python 3.x
- Django 2.x
- PostgreSQL Installation
- Clone the repository: git clone https://github.com/<username>/<repository>.git
- Change into the project directory: cd <repository>
- Create and activate a virtual environment:

```python3 -m venv env```

```source env/bin/activate```
- Install the dependencies: `pip install -r requirements.txt`
- Create a new PostgreSQL database and update the settings in settings.py
- Run migrations: `python manage.py makemigrations` & `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Run the server: `python manage.py runserver`
## Usage
1. Create a new link by visiting http://localhost:8000/create/
2. Use the shortened link and track clicks on it
3. View your links and click data on the dashboard http://localhost:8000/dashboard/
## Features
- User registration and authentication
- Shortening of URLs
- Tracking of clicks on shortened links
- Expiration of links
- Future Improvements
- Adding more statistics and charts for link clicks
- Adding option for custom URLs
- Integrating with external link shortening services
- Allowing users to track clicks on multiple domains
## Contributing
### Fork the repository
1. Create your feature branch: `git checkout -b new-feature`
2. Commit your changes: `git commit -am 'Add some feature'`
3. Push to the branch: `git push origin new-feature`
4. Submit a pull request