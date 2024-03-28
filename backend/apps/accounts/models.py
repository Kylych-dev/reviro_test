from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

from apps.accounts.manager import UserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    role = models.CharField(choices=ROLE_CHOICES, max_length=15, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    profile = models.ImageField(
        upload_to="profile/", null=True, blank=True, verbose_name=_("Profile"))
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."),)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    updated_at = models.DateTimeField(_("date updated"), auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("date_joined",)
        verbose_name = _("user")
        verbose_name_plural = _("users")
        app_label = "accounts"


    def __str__(self):
        return f"{self.get_full_name()}"

    def get_full_name(self):
        """
        Возвращает полное имя пользователя.        
        """
        full_name = "%s %s %s" % (self.first_name, self.last_name, self.email)
        return full_name.strip()

    def get_short_name(self):
        """
        Возвращает короткое имя пользователя.
        """        
        return self.first_name
