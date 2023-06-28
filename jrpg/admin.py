from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher', 'console', 'adaptation']
    list_filter = ['console']
    search_fields = ['name', 'publisher']


admin.site.register(Game, GameAdmin)
