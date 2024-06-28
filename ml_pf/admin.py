from django.contrib import admin

from .models import Education, Location, Date

admin.site.register([Education, Location, Date])
