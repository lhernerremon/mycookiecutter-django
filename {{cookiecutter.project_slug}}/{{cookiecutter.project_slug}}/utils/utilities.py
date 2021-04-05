# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.files import File

# Utils
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import random
from string import digits


def send_email(template: str, subject: str, ctx: dict, to: list):
    from_email = settings.DEFAULT_FROM_EMAIL
    content = render_to_string(template, ctx)
    msg = EmailMultiAlternatives(subject, content, from_email, to)
    msg.attach_alternative(content, "text/html")
    msg.send()
    return msg


def render_img_from_url(picture_url: str):
    name_random = "".join(random.choices(digits, k=5))
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urlopen(picture_url).read())
    img_temp.flush()
    return f"image_{name_random}.png", File(img_temp)
