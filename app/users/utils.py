import os
import secrets
from mailbox import Message
from PIL import Image
from app import mail
from app.secrets import MAIL_USER
from flask import current_app, url_for

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def url_for(param, token, _external):
    pass


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender=MAIL_USER, recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}

If you did not make this  request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)