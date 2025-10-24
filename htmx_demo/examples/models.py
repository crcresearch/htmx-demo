"""Models for demonstration purposes in the examples app."""

from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """Contact model for form submission and search examples."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    """Product model for infinite scroll and search examples."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=50,
        choices=[
            ("electronics", "Electronics"),
            ("clothing", "Clothing"),
            ("books", "Books"),
            ("home", "Home & Garden"),
            ("sports", "Sports"),
        ],
    )
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task model for dynamic list operations example."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["completed", "-created_at"]

    def __str__(self):
        return self.title

    def toggle_complete(self):
        """Toggle task completion status."""
        self.completed = not self.completed
        self.completed_at = timezone.now() if self.completed else None
        self.save()


class Country(models.Model):
    """Country model for dependent dropdown example."""

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(models.Model):
    """State/Province model for dependent dropdown example."""

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.country.code}"


class City(models.Model):
    """City model for dependent dropdown example."""

    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}, {self.state.code}"


class SystemStatus(models.Model):
    """System status model for polling/auto-refresh example."""

    service_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ("operational", "Operational"),
            ("degraded", "Degraded Performance"),
            ("partial_outage", "Partial Outage"),
            ("major_outage", "Major Outage"),
        ],
        default="operational",
    )
    response_time_ms = models.IntegerField(default=0)
    uptime_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    last_check = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "System statuses"
        ordering = ["service_name"]

    def __str__(self):
        return f"{self.service_name}: {self.status}"

