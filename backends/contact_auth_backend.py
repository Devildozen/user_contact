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
            user = Contact._default_manager.get(params).user
        except (Contact.DoesNotExist, User.DoesNotExist):
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
