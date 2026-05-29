from django.contrib import admin

from .models import Product
from .models import Category
from .models import Profile
from .models import Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Review)