# Sample Data Fixture

This directory contains a Django fixture with curated, realistic data for all HTMX training examples.

## What's Included

### Contacts (8 entries)
Realistic tech industry professionals with companies, emails, and inquiry messages:
- Sarah Chen from TechCorp Industries
- Marcus Johnson from Innovate AI
- Emily Rodriguez from CloudNative Solutions
- David Kim from Startup Accelerator
- And more...

### Products (20 entries)
Diverse product catalog across 5 categories:
- **Electronics** (8): Keyboards, monitors, headphones, accessories
- **Books** (3): Programming classics (Clean Code, Pragmatic Programmer, etc.)
- **Clothing** (2): Developer-themed apparel
- **Home & Garden** (4): Office furniture, desk accessories, plants
- **Sports** (3): Fitness equipment and gear

Price range: $29.99 - $799.99  
Includes both in-stock and out-of-stock items for realistic demos.

### Tasks (7 entries)
Mix of completed and pending developer tasks:
- ✅ Update project documentation (completed)
- ✅ Fix bug in user dashboard (completed)
- ⏳ Review pull requests from team (pending)
- ⏳ Refactor authentication module (pending)
- And more...

### Geographic Data
Complete country/state/city hierarchy for cascading dropdown examples:

**United States** (5 states, 17 cities)
- California: San Francisco, Los Angeles, San Diego, Sacramento
- New York: NYC, Buffalo, Rochester
- Texas: Houston, Austin, Dallas, San Antonio
- Florida: Miami, Orlando, Tampa
- Washington: Seattle, Spokane, Tacoma

**Canada** (3 provinces, 6 cities)
- Ontario: Toronto, Ottawa
- British Columbia: Vancouver, Victoria
- Quebec: Montreal, Quebec City

### System Status (6 services)
Realistic microservices monitoring dashboard:
- API Gateway - Operational (42ms)
- Database Cluster - Operational (8ms)
- Authentication Service - Operational (15ms)
- File Storage - Degraded (234ms) ⚠️
- Email Service - Operational (125ms)
- Search Engine - Operational (67ms)

## Loading the Fixture

### From Project Root

```bash
python manage.py loaddata sample_data
```

### With Docker

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py loaddata sample_data
```

### With uv

```bash
uv run python manage.py loaddata sample_data
```

## Resetting Data

To reload the fixture (this will delete existing data):

```bash
# Delete the database
rm db.sqlite3

# Run migrations
python manage.py migrate

# Load the fixture
python manage.py loaddata sample_data
```

## Customizing the Fixture

To modify the data:

1. Edit `sample_data.json` directly
2. Or load data in Django admin, then export:

```bash
python manage.py dumpdata examples --indent 2 > htmx_demo/examples/fixtures/sample_data.json
```

### Exporting Specific Models

```bash
# Export only contacts
python manage.py dumpdata examples.contact --indent 2 > contacts.json

# Export only products
python manage.py dumpdata examples.product --indent 2 > products.json
```

## Fixture Format

The fixture is in Django's JSON format:

```json
[
  {
    "model": "examples.contact",
    "pk": 1,
    "fields": {
      "first_name": "Sarah",
      "last_name": "Chen",
      "email": "sarah.chen@techcorp.com",
      ...
    }
  },
  ...
]
```

## Why Use Fixtures?

**Advantages over random data generation:**
- ✅ **Consistent data** - Same results every time
- ✅ **Realistic content** - Hand-crafted, meaningful data
- ✅ **Perfect for demos** - Professional-looking examples
- ✅ **Version controlled** - Track changes to sample data
- ✅ **Fast loading** - Instant database population
- ✅ **Testing friendly** - Predictable test data

**When to use random generation instead:**
- Need large datasets (100+ items)
- Testing with varied data
- Load testing scenarios
- Don't care about content quality

## Troubleshooting

### Fixture Loading Fails

If you get errors loading the fixture:

1. **Check migrations are current:**
   ```bash
   python manage.py migrate
   ```

2. **Verify the fixture file exists:**
   ```bash
   ls -la htmx_demo/examples/fixtures/sample_data.json
   ```

3. **Check for database conflicts:**
   - Primary key conflicts? Delete existing data or drop the database
   - Foreign key issues? Make sure related objects exist first

### Primary Key Conflicts

If you get "Duplicate key" errors:

```bash
# Option 1: Clear specific tables
python manage.py shell
>>> from htmx_demo.examples.models import *
>>> Contact.objects.all().delete()
>>> Product.objects.all().delete()
# etc...

# Option 2: Start fresh
rm db.sqlite3
python manage.py migrate
python manage.py loaddata sample_data
```

## Adding More Data

To add additional sample data:

1. Load the current fixture
2. Add new data through Django admin or shell
3. Export everything:
   ```bash
   python manage.py dumpdata examples --indent 2 > sample_data.json
   ```
4. Move the file to the fixtures directory

Or edit `sample_data.json` directly and increment the `pk` values.

## Related Commands

```bash
# List all fixtures Django can find
python manage.py loaddata --help

# Load multiple fixtures
python manage.py loaddata fixture1 fixture2

# Dump all data from the examples app
python manage.py dumpdata examples --indent 2

# Dump specific models with natural keys
python manage.py dumpdata examples.country examples.state examples.city \
  --natural-foreign --indent 2
```

## Using in Tests

```python
from django.test import TestCase

class ExampleTests(TestCase):
    fixtures = ['sample_data']
    
    def test_product_search(self):
        # Fixture data is automatically loaded
        from htmx_demo.examples.models import Product
        self.assertEqual(Product.objects.count(), 20)
```

## Data Privacy

All data in this fixture is fictional:
- Email addresses use example domains
- Phone numbers are in the reserved range (+1-555-xxxx)
- Names and companies are fabricated
- No real personal information is included

Safe for public repositories and demos! 🎉

