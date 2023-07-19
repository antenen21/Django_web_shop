from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.safestring import mark_safe                   # img in admin
from django.template.defaultfilters import truncatechars        # img in admin


class Category(models.Model):
    name = models.CharField(max_length=100, )

    def __str__(self):
        return self.name







class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='product_images/')


        # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin

    def __str__(self):
        return self.name









class Fournisseur(models.Model):
    name = models.CharField(max_length=40, null=True)
    street = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=5, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f""" company name :  {self.name}
                    street:         {self.street}
                    postal Code:    {self.postal_code}
                    city:           {self.city}
                    country:        {self.country}
                    phone:          {self.phone}"""

    class Meta:
        ordering = ['my_order']
        verbose_name_plural = "Fournisseur/shipper"








class Pump(models.Model):

    model = models.CharField(max_length=50, null=True)
    power = models.IntegerField(blank=True, default=0)
    description = models.TextField(blank=True)
    COP = models.FloatField(blank=True, default=0.0)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=9)
    # folder is created auto.. in the media folder we create
    img = models.ImageField(upload_to="products", blank=True, null=True)
    # and asign in the settings.py
    date = models.DateField(auto_now=True, null=True)
    slug = models.SlugField(default="", blank=True, null=False)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin


    def get_absolute_url(self):
        return reverse('detail-pump-path', args=[self.slug])

    def __str__(self):
        return f"Model: {self.model}, power: {self.power}kW, Price: {self.price}, COP: {self.COP},  .......       description: .........     {self.description}"









class Puffer(models.Model):
    model = models.CharField(max_length=80)
    capacity = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, default=00.00)
    img = models.ImageField(upload_to="products", blank=True, null=True)
    date = models.DateField(auto_now=True, null=True)
    slug = models.SlugField(default="", blank=True, null=False)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )


        # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin

    def get_absolute_url(self):
        return reverse('detail-puffer-path', args=[self.slug])

    class Meta:
        ordering = ['my_order']














class Review(models.Model):

    user_name = models.CharField(max_length=30, null=True, blank=False)
    comment = models.TextField(max_length=200, null=True, blank=False)
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"username: {self.user_name}, comment: {self.comment}, rating: {self.rating}"

    class Meta:
        ordering = ['my_order']















class ServiceAddons(models.Model):

    name = models.CharField(max_length=50, blank=True, null=False)
    price = models.CharField(max_length=50, blank=True, null=False)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="products", blank=True, null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

        # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin    














class CompleteSet(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    price = models.CharField(max_length=50, blank=True, null=False)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="products", blank=True, null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

        # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin    











class SingleMaterial(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    price = models.CharField(max_length=50, blank=True, null=False)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="products", blank=True, null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True, null=False)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

        # img in admin
        # in template you can use {{ object.description|truncatewords:50 }} for short description    
    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
    # img in admin    
