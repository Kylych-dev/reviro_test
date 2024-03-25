from django.db import models
from django.utils.text import slugify
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.manager import UserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    profile = models.ImageField(
        upload_to="profile/", null=True, blank=True, verbose_name=_("Profile")
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    verification_code = models.CharField(
        verbose_name=_("verification code"), null=True, blank=True, max_length=6
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    updated_at = models.DateTimeField(_("date updated"), auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ("date_joined",)
        verbose_name = _("user")
        verbose_name_plural = _("users")
        app_label = "accounts"


    def save(self, *args, **kwargs):
        if not self.slug:
            unique_date = self.date_joined.toordinal()
            self.slug = slugify(f"{self.id}{unique_date}{self.date_joined.strftime('%H%M%S%D')}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_full_name()}"

    def get_full_name(self):
        """
        Возвращает полное имя пользователя.        
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Возвращает короткое имя пользователя.
        """        
        return self.first_name

