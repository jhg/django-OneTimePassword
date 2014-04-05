from django.conf import settings
from django.contrib.auth import get_user_model
from conf import OTP_TIME_SYNCHRONIZED


class OneTimePassword(object):
    """
    Authenticate with a pseudorandom one time password
    """

    def authenticate(self, username=None, password=None, *args, **kwargs):
        if username != None and password != None:
            if OTP_TIME_SYNCHRONIZED.get_user_password(username) == password:
                user_model = get_user_model()
                search_user = {user_model.USERNAME_FIELD: username}
                try:
                    return user_model.objects.get(**search_user)
                except User.DoesNotExist:
                    return None
        return None

    def get_user(self, user_id, *args, **kwargs):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class TwoFactorAuthentication(object):
    """
    Authenticate with a pseudorandom two factor authentication
    """

    def authenticate(self, username=None, password=None, token=None, *args, **kwargs):
        if username != None and password != None and token != None:
            if OTP_TIME_SYNCHRONIZED.get_user_password(username) == token:
                user_model = get_user_model()
                search_user = {user_model.USERNAME_FIELD: username}
                try:
                    user = user_model.objects.get(**search_user)
                except User.DoesNotExist:
                    return None
                if user.check_password(password):
                    return user
        return None

    def get_user(self, user_id, *args, **kwargs):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
