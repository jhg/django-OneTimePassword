from django.conf import settings
from django.contrib.auth import get_user_model
from django_OneTimePassword.gen_password import sha512TS


class PasswordTimeSynchronized(object):
    """
    Authenticate with a password time synchronized
    """

    def authenticate(self, username=None, password=None):
        if username != None and password != None:
            instance = sha512TS()
            if instance.get_user_password(username) == password:
                user_model = get_user_model()
                search_user = {user_model.USERNAME_FIELD: username}
                try:
                    return user_model.objects.get(**search_user)
                except User.DoesNotExist:
                    return None
        return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
