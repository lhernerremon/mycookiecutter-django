# Django
from django.conf import settings
from django.http import HttpRequest
from django.template.loader import render_to_string

# Allauth
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

# Utilities
from typing import Any
from {{ cookiecutter.project_slug }}.utils.utilities import send_email


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def render_mail(self, template_prefix, email, ctx):
        to = [email] if isinstance(email, str) else email
        subject = render_to_string("{0}_subject.txt".format(template_prefix), ctx)
        subject = " ".join(subject.splitlines()).strip()
        template = "{0}_message.html".format(template_prefix)
        msg = send_email(template, subject, ctx, to)
        return msg


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
