from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "years_of_experience",)}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    fields = ("name", "description", "price", "dish_type", "cooks")
    filter_horizontal = ("cooks",)
    list_display = ("name", "price", "dish_type")
    list_filter = ("dish_type",)
    search_fields = ("name",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
