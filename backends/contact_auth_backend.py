from contact.models import Contact, User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class ContactBackend(ModelBackend):

    def get_login_value(self, model, **kwargs):
        value = None
        for field in model.AUTH_FIELDS:
            value = kwargs.get(field)
        return value

    def authenticate(self, username=None, password=None, **kwargs):
        AuthModel = Contact
        if username is None:
            username = self.get_login_value(AuthModel, **kwargs)

        params = Q()
        for field in AuthModel.AUTH_FIELDS:
           params |= Q(**{field: username})

        try:
            contact = Contact._default_manager.get(params)
        except AuthModel.DoesNotExist:
            return None
        else:
            try:
                user = contact.user
            except AuthModel.DoesNotExist:
                return None
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None