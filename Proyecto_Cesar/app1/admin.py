from django.contrib import admin

from .models import pedido, platillo, user

# Register your models here.
admin.site.register(user)
admin.site.register(platillo)
admin.site.register(pedido)