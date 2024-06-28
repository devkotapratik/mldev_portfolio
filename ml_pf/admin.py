from django.contrib import admin

from .models import Education, Location, Date, Image

admin.site.register([Education, Location, Date, Image])
