from django.contrib import admin
from .models import Country, State

class StateInline(admin.TabularInline):
    model = State
    extra = 1

class CountryAdmin(admin.ModelAdmin):
    inlines = [StateInline]
    list_display = ('name', 'code', 'population')
    search_fields = ('name', 'code')
    list_filter = ('continent',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'population', 'country')
    search_fields = ('name', 'code')
    list_filter = ('country',)

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
