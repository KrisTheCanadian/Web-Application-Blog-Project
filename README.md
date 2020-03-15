# Web Application Project

Inspired by [@CoreyMSchafer](https://github.com/CoreyMSchafer) 's Flask Tutorials : [Flask Web Application Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

The goal of this project was to learn how to use create a Web Application using the Flask Framework.

Dependencies:
- Python 3.7+
- Pillow
- flask_login
- flask-bcrypt
- flask-sqlalchemy
- flask-wtf
- flask

Make sure to create app/secrets.py and in your secrets.py add the following:
'''python
SECRET_KEY = 'SOME RANDOM STRING'
'''

Ways to generate a secure random string:
'''sh
python3
>>> import os,binascii
>>> print binascii.b2a_hex(os.urandom(15))
"c84766ca4a3ce52c3602bbf02ad1f7"
'''
