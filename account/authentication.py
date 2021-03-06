from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """Виконує аутенфікацію користувача по е-мейл"""

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class PhoneAuthBackend(object):
    """Виконує аутенфікацію користувача за номером телефона"""

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(profile__phone=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None