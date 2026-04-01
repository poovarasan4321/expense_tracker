from django.contrib import admin
from tracker.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    # ✅ Columns you want to show
    list_display = ('user', 'amount', 'type',
                    'category', 'description', 'date')


admin.site.register(Transaction, TransactionAdmin)

# Register your models here.
