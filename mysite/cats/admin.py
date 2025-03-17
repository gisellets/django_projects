from django.contrib import admin

from .models import Cat, Type, Treat
# Register your models here.

admin.site.register(Cat)
admin.site.register(Type)
admin.site.register(Treat)
