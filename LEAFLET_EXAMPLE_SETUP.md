# Quick Setup Guide for Leaflet Interactive Maps Example

## Step 1: Run Migration
```bash
docker-compose -f docker-compose.local.yml run --rm django python manage.py migrate
```

## Step 2: Create Sample Data
```bash
docker-compose -f docker-compose.local.yml run --rm django python manage.py create_sample_data
```

This will create 18 sample San Francisco locations with various categories (restaurants, hotels, museums, parks, shopping, offices).

## Step 3: Start the Development Server
```bash
docker-compose -f docker-compose.local.yml up
```

## Step 4: View the Example
Open your browser and navigate to:
- **Comparison Index:** http://localhost:8000/examples/comparison/
- **Leaflet Map Example:** http://localhost:8000/examples/comparison/mapbox/

## What You'll See

### jQuery/AJAX Implementation (Left Side)
- Filter dropdowns for category, rating, and price
- Interactive Leaflet map with markers
- Manual AJAX calls and JSON parsing
- ~80 lines of code

### HTMX Implementation (Right Side)
- Same filter dropdowns
- Same interactive map
- Declarative HTMX attributes
- ~60 lines of code (25% less!)

## Using the Example

1. **Try the filters:**
   - Select different categories (Restaurant, Hotel, Museum, etc.)
   - Filter by minimum rating (3+, 4+, 4.5+)
   - Filter by price range ($, $$, $$$, $$$$)

2. **Interact with the map:**
   - Click on markers to see location details
   - Zoom and pan the map
   - Notice how both implementations behave identically

3. **Compare the code:**
   - Click the "Code" tab on each side
   - See the implementation differences
   - Notice HTMX's cleaner, more declarative approach

## Why Leaflet?

**No API Token Required!** 
- Uses free OpenStreetMap tiles
- No signup or registration needed
- No usage limits or billing
- 100% open source
- Works immediately out of the box

## Adding More Locations

### Via Django Admin
1. Go to http://localhost:8000/admin/
2. Navigate to "Locations"
3. Click "Add Location"
4. Fill in the details (name, address, coordinates, category, etc.)
5. Save and refresh the map

### Via Django Shell
```bash
docker-compose -f docker-compose.local.yml run --rm django python manage.py shell
```

```python
from htmx_demo.examples.models import Location
from decimal import Decimal

Location.objects.create(
    name="Your Location",
    address="123 Main St, San Francisco, CA",
    latitude=Decimal("37.7749"),
    longitude=Decimal("-122.4194"),
    category="restaurant",
    description="A great place",
    rating=Decimal("4.5"),
    price_range="$$"
)
```

## Troubleshooting

### Map not loading
- Check browser console for errors
- Verify sample data was created successfully
- Ensure migrations ran successfully

### No markers appearing
- Verify sample data was created successfully
- Check the browser network tab for API responses
- Make sure you ran the migrations

### Filters not working
- Clear browser cache
- Check browser console for JavaScript errors
- Verify HTMX is loaded (check page source)

## Resources

- Leaflet docs: https://leafletjs.com/
- OpenStreetMap: https://www.openstreetmap.org/
- HTMX docs: https://htmx.org/

