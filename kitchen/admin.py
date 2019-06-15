from django.contrib import admin
from kitchen.models import Week, Dish, Day, Order


class WeekAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Week, WeekAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Order)

