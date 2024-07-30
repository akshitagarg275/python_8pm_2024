from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('tea_name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_vertical = ('chai_varieties',)


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
