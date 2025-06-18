from django.contrib import admin

from cleaning.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','address','email','phone','service','date_and_time','payment_type','status','cancellation_reason')
    list_filter = ('user','address','email','phone','service','date_and_time','payment_type','status','cancellation_reason')
    search_fields = ('user__username','address','email','phone','service','date_and_time','payment_type','status','cancellation_reason')