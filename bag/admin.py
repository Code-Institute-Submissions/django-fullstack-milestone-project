from django.contrib import admin
from .models import Bonus
# Register your models here.


class BonusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'expires_on',
        'description',
        'amount',
        'created_at',
    )


admin.site.register(Bonus, BonusAdmin)
