django-OneTimePassword
======================

Django One Time Password is authentication backend for use one time passwords.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_OneTimePassword" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'django_OneTimePassword',
      )

2. Include the backend in your AUTHENTICATION_BACKENDS settings like this::

      'django_OneTimePassword.backends.OneTimePassword',
