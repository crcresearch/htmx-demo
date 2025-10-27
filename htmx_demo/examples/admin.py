"""Admin configuration for the examples app."""

from django.contrib import admin

from .models import City
from .models import Contact
from .models import Country
from .models import Location
from .models import Notification
from .models import Product
from .models import State
from .models import SystemStatus
from .models import Task


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "company", "created_at")
    search_fields = ("first_name", "last_name", "email", "company")
    list_filter = ("created_at",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "in_stock", "created_at")
    search_fields = ("name", "description")
    list_filter = ("category", "in_stock", "created_at")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at", "completed_at")
    search_fields = ("title", "description")
    list_filter = ("completed", "created_at")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "country")
    search_fields = ("name", "code")
    list_filter = ("country",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state")
    search_fields = ("name",)
    list_filter = ("state__country",)


@admin.register(SystemStatus)
class SystemStatusAdmin(admin.ModelAdmin):
    list_display = ("service_name", "status", "response_time_ms", "uptime_percentage", "last_check")
    list_filter = ("status",)
    search_fields = ("service_name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "rating", "price_range", "latitude", "longitude")
    search_fields = ("name", "address", "description")
    list_filter = ("category", "rating", "price_range")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message", "notification_type", "created_at", "is_read")
    list_filter = ("notification_type", "is_read", "created_at")
    search_fields = ("message",)
    date_hierarchy = "created_at"

