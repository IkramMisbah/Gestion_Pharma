from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Produits)
admin.site.register(Vente)
admin.site.register(Customers)
admin.site.register(Facture_Client)