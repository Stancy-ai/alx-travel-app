from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
from faker import Faker
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create or get a test user
        user, _ = User.objects.get_or_create(username="testuser", defaults={"password": "testpass"})

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=random.randint(50, 500),
                owner=user,
            )

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
