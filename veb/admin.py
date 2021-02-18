from django.contrib import admin
from .models import Events, TematicBlock, Category, Coors

# Register your models here.

admin.site.register(Events)
admin.site.register(Category)
admin.site.register(Coors)

