from django.contrib import admin
from .models import Offer, Market


class OfferAdmin(admin.ModelAdmin):
  list_display = ( 'id', 'rate', 'description')


class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','address',
                    'phon_num')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Market, MarketAdmin)

