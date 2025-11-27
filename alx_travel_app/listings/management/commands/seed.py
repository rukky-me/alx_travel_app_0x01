from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Modern Ocean View Apartment",
                "description": "Beautiful apartment with an amazing sea view.",
                "location": "Victoria Island, Lagos",
                "price_per_night": 45000.00,
                "capacity": 4,
            },
            {
                "title": "Cozy Budget Studio",
                "description": "Small, affordable studio perfect for travelers.",
                "location": "Yaba, Lagos",
                "price_per_night": 15000.00,
                "capacity": 2,
            },
            {
                "title": "Luxury 4-Bedroom Duplex",
                "description": "Fully serviced duplex in a quiet estate.",
                "location": "Lekki Phase 1, Lagos",
                "price_per_night": 120000.00,
                "capacity": 6,
            },
            {
                "title": "Shortlet Room",
                "description": "Simple room for short stays.",
                "location": "Ikeja GRA, Lagos",
                "price_per_night": 20000.00,
                "capacity": 1,
            },
        ]

        # Create sample listings
        for item in sample_listings:
            Listing.objects.create(
                title=item["title"],
                description=item["description"],
                location=item["location"],
                price_per_night=item["price_per_night"],
                capacity=item["capacity"],
                is_active=True,
                created_at=timezone.now(),
            )

        self.stdout.write(self.style.SUCCESS("🎉 Database seeded with sample listings!"))
