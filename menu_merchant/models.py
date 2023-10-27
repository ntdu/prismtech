from django.conf import settings
from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name_vi = models.CharField(max_length=50, default="SOME STRING")
    name_en = models.CharField(max_length=50, default="SOME STRING")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="category")
    notes = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    hashtag = models.OneToOneField(Hashtag, on_delete=models.CASCADE, null=True, blank=True, related_name="category")
    image = models.CharField(default=None, null=True, blank=True, max_length=1000)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_en}, parent: {self.parent}"

class Merchant(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="merchants", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=45, null=True, blank=True)
    country_code = models.CharField(max_length=4, null=True, blank=True)
    country_number = models.CharField(max_length=4, null=True, blank=True)
    platform_number = models.CharField(max_length=45, null=True, blank=True)
    website = models.CharField(null=True, blank=True, max_length=255)
    uid = models.CharField(max_length=64, null=True, blank=True, unique=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    hashtags = models.ManyToManyField("menu_merchant.Hashtag", blank=True, related_name="merchants")
    categories = models.ManyToManyField("menu_merchant.Category", blank=True, related_name="merchants")
    keywords = models.ManyToManyField("menu_merchant.Keyword", blank=True, related_name="merchants")
    is_staffs_visible = models.BooleanField(default=True)
    total_available_slot = models.IntegerField(default=0, null=True, blank=True)
    total_available_slots_unit = models.CharField(max_length=45, null=True, blank=True)
    total_bookings = models.IntegerField(default=0, null=True, blank=True)
    opening_date = models.DateTimeField(null=True, blank=True)
    avatar = models.JSONField(default=dict, null=True, blank=True, help_text="Avatar of merchant vio app")
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    banner = models.JSONField(default=dict, null=True, blank=True, help_text="Banner")
    allow_staff_connect_user = models.BooleanField(default=False)
    note_placeholder = models.TextField(null=True, blank=True, help_text="Booking note for your client")

class Promotion(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default=None, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=False)
    end_date = models.DateTimeField(null=True, blank=False)
    discount = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=255, null=True, blank=True, default=None)
    quantity = models.IntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=255, null=True, blank=True, default="discount")
    buy_quantity = models.IntegerField(null=True, blank=True)
    get_quantity = models.IntegerField(null=True, blank=True)
    images = models.JSONField(default=list, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, blank=True, related_name="promotion")
    products = models.ManyToManyField("Product", blank=True, related_name="promotions")
    services = models.ManyToManyField("Service", blank=True, related_name="promotions")
    total_bookings = models.IntegerField(default=0, null=True, blank=True)
    all_day = models.BooleanField(default=False)
    is_happy_hour = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    hashtags = models.ManyToManyField(Hashtag, related_name="products", blank=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255, null=True, default=None)
    description = models.TextField(null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    original_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, null=True, blank=True)
    images = models.JSONField(default=list, null=True, blank=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    keywords = models.ManyToManyField(Keyword, blank=True, related_name="products")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    total_bookings = models.IntegerField(default=0, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold_quantity = models.IntegerField(default=0, help_text="Product sold quantity")

    def __str__(self):
        if self.name:
            return self.name
        return f"Product ID=[{self.id}]"


class Service(models.Model):
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="services")
    keywords = models.ManyToManyField(Keyword, blank=True, related_name="services")
    hashtags = models.ManyToManyField(Hashtag, related_name="services", blank=True)
    description = models.TextField(null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    time = models.FloatField()
    time_date = models.CharField(max_length=255, null=True, default=None)
    require_staff = models.BooleanField(default=False)
    original_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, null=True, blank=True)
    available_slots = models.IntegerField()
    slots_unit = models.CharField(max_length=50, null=False, blank=True)
    use_total_available_slots = models.BooleanField(default=False)
    images = models.JSONField(default=list, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    flexible_time = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    total_bookings = models.IntegerField(default=0, null=True, blank=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name="services")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold_quantity = models.IntegerField(default=0, null=True, blank=True, help_text="Service sold quantity")

    def __str__(self):
        if self.name:
            return self.name
        return f"Service ID=[{self.id}]"


class Collection(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True, related_name="collection")
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)