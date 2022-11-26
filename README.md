# Final version of Yatube API
Yatube is study pet-project created in order to get familiar with Python, Django, DRF and related technologies.
It hase functionality of simple, yet quick and effective web-blog with modern security methods and ready to deploy.
This is API part.
You can build a mobile or desktop app using this API or integrate Yatube blog with your web-app.

#### Installation:
To install virtual environmet and dependencies run next script from project folder:
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
  
Then run the Django server using next command:
 ```sh
python3 <path to your manage.py file> runserver
```
  
When server is running, API documentation will be availiable at [ReDoc url](http://127.0.0.1:8000/redoc/).  
To deploy it on server using external IP our suggestion is to use Nginx and Gunicorn. Make sure to update Django settings file according to Django documentation.

##### Made by Artem Sinitsyn, curated by Ya.Practicum.
