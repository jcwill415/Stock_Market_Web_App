from django.contrib import admin
from .models import Stock

admin.site.register(Stock) # pass in Stock class from models.py