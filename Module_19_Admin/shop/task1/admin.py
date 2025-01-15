from django.contrib import admin
from .models import Buyer, Game


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('size', 'cost')
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'size')
        }),
        ('Дополнительные настройки', {
            'fields': ('age_limited', 'description')
        })
    )


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_filter = ('balance', 'age')
    list_per_page = 30

    readonly_fields = ('balance',)

