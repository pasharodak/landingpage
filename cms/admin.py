from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider
# Register your models here.

class CmsAdm(admin.ModelAdmin):
    list_display = ("cms_title","cms_text","cms_css","img_field")
    fields = ("cms_title","cms_text","cms_css","cms_img","img_field")
    readonly_fields = ("img_field",)

    def img_field (self,obj):
        return mark_safe(f'<img src= "{obj.cms_img.url}" width = "80px"')

admin.site.register(CmsSlider, CmsAdm)