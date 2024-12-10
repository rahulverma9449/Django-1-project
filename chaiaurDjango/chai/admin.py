from django.contrib import admin
from .models import ChaiVarieties, ChaiReview,Store,ChaiCertificate, Order

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaivarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCartificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number','issued_date','valid_untill')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'chai', 'date_ordered', 'complete', 'transaction_id')
    list_filter = ('date_ordered', 'complete')

admin.site.register(Order)
admin.site.register(ChaiVarieties, ChaivarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiReview)
admin.site.register(ChaiCertificate, ChaiCartificateAdmin)
