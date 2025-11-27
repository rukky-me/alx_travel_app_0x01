from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.title} - {self.location}"

    @property
    def average_rating(self):
        agg = self.reviews.aggregate(avg=models.Avg('rating'))
        return agg['avg'] or 0

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"

    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, null=True, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # This guarantees check_out is only after check_in
        if self.check_out <= self.check_in:
            raise ValueError("check_out must be after check_in")
        # This ensures that guests do not exceed the listing capacity
        if self.listing and self.guests > self.listing.capacity:
            raise ValueError("guests may not exceed listing capacity")

    def save(self, *args, **kwargs):
        # this will compute total_price: nights * price_per_night
        nights = (self.check_out - self.check_in).days
        self.total_price = nights * self.listing.price_per_night
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Booking for {self.listing.title} from {self.check_in} to {self.check_out}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'listing'], name='unique_user_listing_review')
        ]

    def __str__(self) -> str:
        username = self.user.username if self.user else "Anonymous"
        return f"Review {self.rating}/5 by {username} on {self.listing.title}"