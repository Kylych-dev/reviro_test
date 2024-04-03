from django.contrib import admin
from .models import CustomUser 


admin.site.register(CustomUser)
# admin.site.register(RegularUser)
# admin.site.register(ChatMessage)
# admin.site.register(Partner)



'''
вот модели



class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=15, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
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
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ("date_joined",)
        verbose_name = _("user")
        verbose_name_plural = _("users")
        app_label = "accounts"


    def __str__(self):
        return f"{self.email}"


        
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity_in_stock = models.IntegerField(verbose_name="Quantity in Stock")
    availability_status = models.BooleanField(default=True, verbose_name="Availability Status")
    category = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name="Review Text")
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Rating")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ['user', 'product']  # Each user can write only one review for a product

    def __str__(self):
        return f"Review by {self.user} for {self.product}"


class Store(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    locations = models.CharField(max_length=255, verbose_name="Locations")
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='establishments')

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name

покажи код представления и сериализатора?


'''