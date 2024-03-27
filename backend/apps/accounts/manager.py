from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, role=None, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not password:
            raise ValueError(_("The password must be set"))
    
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        if role:
            user.role = role
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password=password, **extra_fields)
