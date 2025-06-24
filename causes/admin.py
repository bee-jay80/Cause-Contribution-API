from django.contrib import admin
from .models import Cause, Contribute

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image_url')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('image_url',)

@admin.register(Contribute)
class ContributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cause', 'name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email', 'cause__title')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    
    def cause(self, obj):
        return obj.cause.title if obj.cause else "No Cause"