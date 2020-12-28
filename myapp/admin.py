from django.contrib import admin

# Register your models here.
from .models import Artist, Event
 

admin.site.register(Artist)
admin.site.register(Event)

