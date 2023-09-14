from django.contrib import admin
from .models import Order, StatusCRM, ComentCRM
# Register your models here.

class Coment(admin.StackedInline):
    model = ComentCRM
    fields = ("coment_text", "coment_dt")
    readonly_fields = ("coment_dt",)
    extra = 0

class OrderAdm(admin.ModelAdmin):
    list_display = ("order_name","order_phone","order_date","order_status")
    list_display_links =("order_name",)
    list_filter = ("order_status",)
    list_max_show_all = 100
    search_fields = ("order_name","order_phone",)
    list_editable = ("order_status",)
    list_per_page = 10
    fields = ("order_name","order_phone","order_date")
    readonly_fields = ("order_date",)
    inlines = [Coment,]

admin.site.register(Order,OrderAdm)

admin.site.register(StatusCRM)
admin.site.register(ComentCRM)
