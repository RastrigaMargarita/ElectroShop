from django.contrib import admin

from company.models import Company, Country, Town


@admin.action(description="Очистить задолженность")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'category',
                    'title',
                    'email',
                    'country',
                    'town',
                    'street',
                    'building',
                    'get_products',
                    'supplier',
                    'debt',
                    'created')
    fields = ('category',
              'title',
              'email',
              'country',
              'town',
              'street',
              'building',
              'products',
              'supplier',
              'debt')
    list_display_links = ['supplier', ]

    list_filter = ['town']
    actions = [clear_debt]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title')


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title')
