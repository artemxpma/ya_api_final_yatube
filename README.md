# Final version of Yatube API
This is latest version of API part for Yatube project.
You can build a mobile or desktop app using this API or integrate Yatube blog with your web-app.

#### To install
virtual environmet and dependencies run next script from project folder:
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then run the django server using
 ```sh
python3 <path to manage.py file> runserver
```
After this API documentation will be availiable at redoc on your [local server](http://127.0.0.1:8000/redoc/)