"""Management command to create sample data for the examples app."""

from decimal import Decimal

from django.core.management.base import BaseCommand

from htmx_demo.examples.models import City
from htmx_demo.examples.models import Contact
from htmx_demo.examples.models import Country
from htmx_demo.examples.models import Location
from htmx_demo.examples.models import Product
from htmx_demo.examples.models import State
from htmx_demo.examples.models import SystemStatus
from htmx_demo.examples.models import Task


class Command(BaseCommand):
    help = "Creates sample data for HTMX examples"

    def handle(self, *args, **options):
        self.stdout.write("Creating sample data...")

        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Contact.objects.all().delete()
        Product.objects.all().delete()
        Task.objects.all().delete()
        City.objects.all().delete()
        State.objects.all().delete()
        Country.objects.all().delete()
        SystemStatus.objects.all().delete()
        Location.objects.all().delete()

        # Create Contacts
        self.stdout.write("Creating contacts...")
        contacts_data = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "phone": "555-0101",
                "company": "Acme Corp",
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane.smith@example.com",
                "phone": "555-0102",
                "company": "Tech Solutions",
            },
            {
                "first_name": "Bob",
                "last_name": "Johnson",
                "email": "bob.johnson@example.com",
                "phone": "555-0103",
                "company": "Global Industries",
            },
            {
                "first_name": "Alice",
                "last_name": "Williams",
                "email": "alice.williams@example.com",
                "phone": "555-0104",
                "company": "Innovate Inc",
            },
            {
                "first_name": "Charlie",
                "last_name": "Brown",
                "email": "charlie.brown@example.com",
                "phone": "555-0105",
                "company": "StartUp Co",
            },
            {
                "first_name": "Diana",
                "last_name": "Davis",
                "email": "diana.davis@example.com",
                "phone": "555-0106",
                "company": "Enterprise LLC",
            },
            {
                "first_name": "Eve",
                "last_name": "Martinez",
                "email": "eve.martinez@example.com",
                "phone": "555-0107",
                "company": "Consulting Group",
            },
            {
                "first_name": "Frank",
                "last_name": "Garcia",
                "email": "frank.garcia@example.com",
                "phone": "555-0108",
                "company": "Dev Agency",
            },
            {
                "first_name": "Grace",
                "last_name": "Rodriguez",
                "email": "grace.rodriguez@example.com",
                "phone": "555-0109",
                "company": "Design Studio",
            },
            {
                "first_name": "Henry",
                "last_name": "Wilson",
                "email": "henry.wilson@example.com",
                "phone": "555-0110",
                "company": "Software Labs",
            },
        ]

        for i, contact_data in enumerate(contacts_data, 1):
            Contact.objects.create(**contact_data)
            if i % 5 == 0:
                # Add some variety
                Contact.objects.create(
                    first_name=f"User{i}",
                    last_name=f"Test{i}",
                    email=f"user{i}@test.com",
                    phone=f"555-{i:04d}",
                    company=f"Company {i}",
                )

        self.stdout.write(self.style.SUCCESS(f"Created {Contact.objects.count()} contacts"))

        # Create Products
        self.stdout.write("Creating products...")
        categories = ["electronics", "clothing", "books", "home", "sports"]
        product_templates = {
            "electronics": [
                ("Laptop Pro 15", "High-performance laptop with 16GB RAM", 1299.99),
                ("Wireless Mouse", "Ergonomic wireless mouse with precision tracking", 29.99),
                ("USB-C Hub", "7-in-1 USB-C hub with HDMI and ethernet", 49.99),
                ("Mechanical Keyboard", "RGB backlit mechanical keyboard", 89.99),
                ("Webcam HD", "1080p webcam with built-in microphone", 69.99),
            ],
            "clothing": [
                ("Cotton T-Shirt", "Comfortable 100% cotton t-shirt", 19.99),
                ("Denim Jeans", "Classic fit denim jeans", 49.99),
                ("Running Shoes", "Lightweight running shoes", 79.99),
                ("Hoodie", "Warm fleece hoodie", 39.99),
                ("Baseball Cap", "Adjustable baseball cap", 14.99),
            ],
            "books": [
                ("Python Programming", "Complete guide to Python programming", 39.99),
                ("Web Development 101", "Introduction to web development", 29.99),
                ("Data Science Handbook", "Comprehensive data science resource", 49.99),
                ("JavaScript Guide", "Modern JavaScript techniques", 34.99),
                ("SQL Fundamentals", "Database fundamentals and SQL", 44.99),
            ],
            "home": [
                ("Coffee Maker", "Programmable coffee maker with timer", 79.99),
                ("Desk Lamp", "LED desk lamp with adjustable brightness", 34.99),
                ("Storage Bins", "Set of 4 stackable storage bins", 24.99),
                ("Wall Clock", "Modern minimalist wall clock", 29.99),
                ("Throw Pillow", "Decorative throw pillow", 19.99),
            ],
            "sports": [
                ("Yoga Mat", "Non-slip yoga mat with carrying strap", 29.99),
                ("Dumbbells Set", "Adjustable dumbbell set 10-50 lbs", 149.99),
                ("Water Bottle", "Insulated stainless steel water bottle", 24.99),
                ("Resistance Bands", "Set of 5 resistance bands", 19.99),
                ("Jump Rope", "Speed jump rope for cardio", 14.99),
            ],
        }

        for category in categories:
            for name, description, price in product_templates[category]:
                Product.objects.create(
                    name=name,
                    description=description,
                    price=Decimal(str(price)),
                    category=category,
                    in_stock=True,
                )
                # Add some variations
                Product.objects.create(
                    name=f"{name} (Premium)",
                    description=f"{description} - Premium edition",
                    price=Decimal(str(price * 1.5)),
                    category=category,
                    in_stock=True,
                )

        # Add some out of stock items
        for i in range(5):
            Product.objects.create(
                name=f"Unavailable Item {i+1}",
                description="Currently out of stock",
                price=Decimal("99.99"),
                category="electronics",
                in_stock=False,
            )

        self.stdout.write(self.style.SUCCESS(f"Created {Product.objects.count()} products"))

        # Create Tasks
        self.stdout.write("Creating tasks...")
        tasks_data = [
            ("Review pull requests", "Check and merge pending PRs"),
            ("Update documentation", "Add new API endpoints to docs"),
            ("Fix bug in authentication", "Users report login issues"),
            ("Implement search feature", "Add full-text search to products"),
            ("Optimize database queries", "Reduce N+1 queries in listings"),
        ]

        for title, description in tasks_data:
            Task.objects.create(title=title, description=description)

        self.stdout.write(self.style.SUCCESS(f"Created {Task.objects.count()} tasks"))

        # Create Countries, States, and Cities
        self.stdout.write("Creating locations...")

        # United States
        us = Country.objects.create(name="United States", code="US")

        states_us = {
            "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento"],
            "New York": ["New York City", "Buffalo", "Rochester", "Albany"],
            "Texas": ["Houston", "Dallas", "Austin", "San Antonio"],
            "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville"],
            "Illinois": ["Chicago", "Aurora", "Naperville", "Peoria"],
        }

        for state_name, cities in states_us.items():
            state = State.objects.create(
                name=state_name,
                code=state_name[:2].upper(),
                country=us,
            )
            for city_name in cities:
                City.objects.create(name=city_name, state=state)

        # Canada
        canada = Country.objects.create(name="Canada", code="CA")

        states_canada = {
            "Ontario": ["Toronto", "Ottawa", "Mississauga", "Hamilton"],
            "Quebec": ["Montreal", "Quebec City", "Laval", "Gatineau"],
            "British Columbia": ["Vancouver", "Victoria", "Surrey", "Burnaby"],
            "Alberta": ["Calgary", "Edmonton", "Red Deer", "Lethbridge"],
        }

        for state_name, cities in states_canada.items():
            state = State.objects.create(
                name=state_name,
                code=state_name[:2].upper(),
                country=canada,
            )
            for city_name in cities:
                City.objects.create(name=city_name, state=state)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {Country.objects.count()} countries, "
                f"{State.objects.count()} states, "
                f"{City.objects.count()} cities"
            ),
        )

        # Create System Statuses
        self.stdout.write("Creating system statuses...")
        services = [
            {
                "service_name": "Web Application",
                "status": "operational",
                "response_time_ms": 125,
                "uptime_percentage": Decimal("99.98"),
            },
            {
                "service_name": "API Server",
                "status": "operational",
                "response_time_ms": 89,
                "uptime_percentage": Decimal("99.95"),
            },
            {
                "service_name": "Database",
                "status": "operational",
                "response_time_ms": 45,
                "uptime_percentage": Decimal("99.99"),
            },
            {
                "service_name": "Cache Server",
                "status": "operational",
                "response_time_ms": 12,
                "uptime_percentage": Decimal("99.97"),
            },
        ]

        for service in services:
            SystemStatus.objects.create(**service)

        self.stdout.write(self.style.SUCCESS(f"Created {SystemStatus.objects.count()} system statuses"))

        # Create Locations (San Francisco area)
        self.stdout.write("Creating locations...")
        locations_data = [
            {
                "name": "Blue Bottle Coffee",
                "address": "66 Mint St, San Francisco, CA 94103",
                "latitude": Decimal("37.7814"),
                "longitude": Decimal("-122.4078"),
                "category": "restaurant",
                "description": "Artisanal coffee roaster and cafe",
                "rating": Decimal("4.5"),
                "price_range": "$$",
            },
            {
                "name": "Golden Gate Bridge Welcome Center",
                "address": "Golden Gate Bridge, San Francisco, CA 94129",
                "latitude": Decimal("37.8199"),
                "longitude": Decimal("-122.4783"),
                "category": "park",
                "description": "Iconic suspension bridge and landmark",
                "rating": Decimal("5.0"),
                "price_range": "$",
            },
            {
                "name": "Exploratorium",
                "address": "Pier 15, San Francisco, CA 94111",
                "latitude": Decimal("37.8012"),
                "longitude": Decimal("-122.3978"),
                "category": "museum",
                "description": "Interactive science museum",
                "rating": Decimal("4.7"),
                "price_range": "$$",
            },
            {
                "name": "Ferry Building Marketplace",
                "address": "1 Ferry Building, San Francisco, CA 94111",
                "latitude": Decimal("37.7956"),
                "longitude": Decimal("-122.3933"),
                "category": "shopping",
                "description": "Historic marketplace with local vendors",
                "rating": Decimal("4.6"),
                "price_range": "$$",
            },
            {
                "name": "Palace Hotel",
                "address": "2 New Montgomery St, San Francisco, CA 94105",
                "latitude": Decimal("37.7881"),
                "longitude": Decimal("-122.4012"),
                "category": "hotel",
                "description": "Luxury historic hotel in downtown",
                "rating": Decimal("4.4"),
                "price_range": "$$$$",
            },
            {
                "name": "Tartine Bakery",
                "address": "600 Guerrero St, San Francisco, CA 94110",
                "latitude": Decimal("37.7617"),
                "longitude": Decimal("-122.4241"),
                "category": "restaurant",
                "description": "Famous artisan bakery and cafe",
                "rating": Decimal("4.6"),
                "price_range": "$$",
            },
            {
                "name": "Salesforce Tower",
                "address": "415 Mission St, San Francisco, CA 94105",
                "latitude": Decimal("37.7897"),
                "longitude": Decimal("-122.3968"),
                "category": "office",
                "description": "Tallest building in San Francisco",
                "rating": Decimal("4.3"),
                "price_range": "$$$",
            },
            {
                "name": "San Francisco Museum of Modern Art",
                "address": "151 3rd St, San Francisco, CA 94103",
                "latitude": Decimal("37.7857"),
                "longitude": Decimal("-122.4011"),
                "category": "museum",
                "description": "Contemporary and modern art museum",
                "rating": Decimal("4.6"),
                "price_range": "$$$",
            },
            {
                "name": "Fisherman's Wharf",
                "address": "Fisherman's Wharf, San Francisco, CA 94133",
                "latitude": Decimal("37.8080"),
                "longitude": Decimal("-122.4177"),
                "category": "shopping",
                "description": "Waterfront area with shops and restaurants",
                "rating": Decimal("4.2"),
                "price_range": "$$",
            },
            {
                "name": "Alamo Square Park",
                "address": "Hayes St & Steiner St, San Francisco, CA 94117",
                "latitude": Decimal("37.7766"),
                "longitude": Decimal("-122.4340"),
                "category": "park",
                "description": "Park with famous Painted Ladies view",
                "rating": Decimal("4.7"),
                "price_range": "$",
            },
            {
                "name": "Foreign Cinema",
                "address": "2534 Mission St, San Francisco, CA 94110",
                "latitude": Decimal("37.7565"),
                "longitude": Decimal("-122.4188"),
                "category": "restaurant",
                "description": "Upscale restaurant with outdoor films",
                "rating": Decimal("4.5"),
                "price_range": "$$$",
            },
            {
                "name": "The St. Regis San Francisco",
                "address": "125 3rd St, San Francisco, CA 94103",
                "latitude": Decimal("37.7856"),
                "longitude": Decimal("-122.4006"),
                "category": "hotel",
                "description": "Five-star luxury hotel",
                "rating": Decimal("4.6"),
                "price_range": "$$$$",
            },
            {
                "name": "Dolores Park",
                "address": "Mission Dolores Park, San Francisco, CA 94114",
                "latitude": Decimal("37.7596"),
                "longitude": Decimal("-122.4269"),
                "category": "park",
                "description": "Popular urban park with city views",
                "rating": Decimal("4.7"),
                "price_range": "$",
            },
            {
                "name": "Union Square",
                "address": "333 Post St, San Francisco, CA 94108",
                "latitude": Decimal("37.7880"),
                "longitude": Decimal("-122.4074"),
                "category": "shopping",
                "description": "Major shopping district in downtown",
                "rating": Decimal("4.4"),
                "price_range": "$$$",
            },
            {
                "name": "Zuni Café",
                "address": "1658 Market St, San Francisco, CA 94102",
                "latitude": Decimal("37.7721"),
                "longitude": Decimal("-122.4205"),
                "category": "restaurant",
                "description": "Iconic California-Mediterranean restaurant",
                "rating": Decimal("4.4"),
                "price_range": "$$$",
            },
            {
                "name": "Cable Car Museum",
                "address": "1201 Mason St, San Francisco, CA 94108",
                "latitude": Decimal("37.7946"),
                "longitude": Decimal("-122.4113"),
                "category": "museum",
                "description": "Museum about SF's cable car system",
                "rating": Decimal("4.5"),
                "price_range": "$",
            },
            {
                "name": "Pier 39",
                "address": "Beach St & The Embarcadero, San Francisco, CA 94133",
                "latitude": Decimal("37.8087"),
                "longitude": Decimal("-122.4098"),
                "category": "shopping",
                "description": "Tourist attraction with shops and sea lions",
                "rating": Decimal("4.3"),
                "price_range": "$$",
            },
            {
                "name": "The Dorian",
                "address": "2001 Chestnut St, San Francisco, CA 94123",
                "latitude": Decimal("37.8003"),
                "longitude": Decimal("-122.4346"),
                "category": "restaurant",
                "description": "Modern American restaurant in Marina",
                "rating": Decimal("4.3"),
                "price_range": "$$",
            },
        ]

        for location_data in locations_data:
            Location.objects.create(**location_data)

        self.stdout.write(self.style.SUCCESS(f"Created {Location.objects.count()} locations"))

        self.stdout.write(self.style.SUCCESS("\n✅ Sample data created successfully!"))
        self.stdout.write(
            "\nYou can now visit:\n"
            "  - http://localhost:8000/examples/ (landing page)\n"
            "  - http://localhost:8000/examples/comparison/ (side-by-side comparison)\n"
            "  - http://localhost:8000/examples/comparison/mapbox/ (Leaflet map example)\n"
            "  - http://localhost:8000/examples/htmx-deep-dive/ (HTMX deep dive)\n"
        )

