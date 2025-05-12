from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'donation_type', 'payment_method', 'date_donated', 'payment_status')
    list_filter = ('donation_type', 'payment_method', 'payment_status', 'date_donated')
    search_fields = ('name', 'email', 'transaction_id')
    readonly_fields = ('date_donated', 'transaction_id')
    ordering = ('-date_donated',)
