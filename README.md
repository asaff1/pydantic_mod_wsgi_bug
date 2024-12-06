# pydantic mod-wsgi bug

This repository is a minimal reproduction of a bug that occurs when using some pydantic features with mod-wsgi.

This was tested on a Windows machine, with `mod-wsgi==4.9.2`, Python 3.9.9, apache 2.4.57.0

Also tested with Python 3.11 and bug still exists. Tried also `mod_wsgi==5.0.2`.

## Installation
- Get a Windows apache release from https://www.apachelounge.com/download/
- Place your installation at C:/Apache24

Then, install mod-wsgi (Requires VS build tools):
```bash
pip install mod-wsgi==4.9.2
```

```bash
pip install -r requirements.txt
```

### Configure apache
- Open `apache24-django.conf` and replace APP_ROOT to the absolute path of the wsgi.py folder, e.g:  
`DEFINE WSGI_ROOT "C:/your_workspace/pydantic_mod_wsgi_bug/pydantic_mod_wsgi_bug"`
- If you don't use python 3.9 run `mod_wsgi-express module-config` and replace the three lines in `apache24-django.conf` with the output of the command. 

- Start apache server

## Run
Try the endpoints with django dev server, where they will all work:
`python manage.py runserver`
- Browse to `http://localhost:8000/docs`


Then, try the endpoints with apache server, where some of the endpoints will fail:
- Browser to `http://localhost/docs`
The endpoints with string strip and string constraints, will hang, and will actually cause apache to crash. 
- (Check apache error.log, you will see the server has crashed and restarted)