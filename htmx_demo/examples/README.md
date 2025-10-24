# HTMX Examples App

This Django app provides comprehensive, interactive examples comparing jQuery/AJAX with HTMX for common web interaction patterns.

## Overview

The examples app demonstrates 7 key patterns:

1. **Form Submissions** - Contact form with inline validation
2. **Live Search/Filtering** - Real-time search results
3. **Infinite Scroll** - Lazy loading with pagination
4. **Modal Dialogs** - Server-rendered modal content
5. **Dynamic List Operations** - Todo list (add/remove/toggle)
6. **Dependent Dropdowns** - Cascading selects (Country → State → City)
7. **Polling/Auto-refresh** - Live status dashboard

Each pattern is implemented in both jQuery/AJAX and HTMX, allowing side-by-side comparison.

## Setup

### 1. Install Dependencies

The app requires the standard Django stack. All dependencies are already in `pyproject.toml`.

### 2. Run Migrations

```bash
python manage.py makemigrations examples
python manage.py migrate
```

### 3. Load Sample Data

You have two options to populate the database with sample data:

**Option A: Load Fixture (Recommended)**

```bash
python manage.py loaddata sample_data
```

This loads a curated fixture with:
- 8 realistic contacts (tech industry professionals)
- 20 diverse products (electronics, books, clothing, home, sports)
- 7 tasks (mix of completed and pending)
- Country/State/City data (US & Canada with major cities)
- 6 system status services (with various states)

**Option B: Generate Random Data**

```bash
python manage.py create_sample_data
```

This generates larger sample datasets:
- 50 random contacts
- 100 random products
- 20 random tasks
- Country/State/City data (US & Canada)
- System status services

**Note:** You only need to use one option. The fixture provides more realistic, hand-crafted data perfect for demos and training.

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/examples/` to see the examples.

## Page Structure

### Main Pages

- **/examples/** - Landing page with overview
- **/examples/comparison/** - Side-by-side jQuery vs HTMX comparisons
- **/examples/htmx-deep-dive/** - HTMX-focused examples with detailed explanations

### API Endpoints

jQuery/AJAX endpoints (return JSON):
- `GET /examples/api/contacts/search/` - Search contacts
- `GET /examples/api/products/` - Paginated products
- `POST /examples/api/contact/submit/` - Submit contact form
- `POST /examples/api/tasks/create/` - Create task
- `DELETE /examples/api/tasks/<id>/delete/` - Delete task
- And more...

HTMX endpoints (return HTML):
- `GET /examples/htmx/contacts/search/` - Search contacts
- `GET /examples/htmx/products/` - Paginated products
- `POST /examples/htmx/contact/submit/` - Submit contact form
- `POST /examples/htmx/tasks/create/` - Create task
- `DELETE /examples/htmx/tasks/<id>/delete/` - Delete task
- And more...

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **HTMX_GUIDE.md** - Complete HTMX reference with all attributes and patterns
- **COMPARISON_GUIDE.md** - Detailed code comparisons with analysis
- **GOTCHAS.md** - Common pitfalls and how to avoid them

## Using the Examples for Training

### For Instructors

1. **Start with the comparison page** - Show side-by-side examples
2. **Demonstrate each pattern** - Click through and show network requests
3. **Open browser DevTools** - Show the difference in responses (JSON vs HTML)
4. **Review the code** - Walk through both implementations
5. **Use the deep dive page** - For more detailed explanations
6. **Reference the docs** - For comprehensive information

### For Learners

1. **Explore the examples** - Try each interaction
2. **View page source** - See the HTMX attributes in action
3. **Open DevTools Network tab** - Observe the requests and responses
4. **Read the comparisons** - Understand the differences
5. **Experiment** - Modify the code and see what happens
6. **Build your own** - Apply patterns to your projects

## Code Organization

```
htmx_demo/examples/
├── __init__.py
├── admin.py          # Django admin configuration
├── apps.py           # App configuration
├── models.py         # Data models for demos
├── urls.py           # URL routing
├── views.py          # All view logic (jQuery and HTMX)
└── README.md         # This file

htmx_demo/templates/examples/
├── index.html              # Landing page
├── comparison.html         # Side-by-side comparisons
├── htmx_deep_dive.html    # HTMX deep dive
└── partials/              # HTML fragments for HTMX
    ├── form_errors.html
    ├── form_success.html
    ├── contact_results.html
    ├── product_list.html
    ├── product_modal.html
    ├── task_item.html
    ├── state_options.html
    ├── city_options.html
    └── system_status.html

htmx_demo/static/css/
└── examples.css         # Styling for examples

docs/
├── HTMX_GUIDE.md           # Comprehensive HTMX guide
├── COMPARISON_GUIDE.md      # Detailed comparisons
└── GOTCHAS.md              # Common pitfalls
```

## Key Differences: jQuery vs HTMX

### jQuery/AJAX Approach

```javascript
// JavaScript-heavy
$('#search').on('keyup', function() {
  $.ajax({
    url: '/api/search/',
    data: { q: $(this).val() },
    success: function(response) {
      let html = '';
      response.results.forEach(item => {
        html += `<div>${item.name}</div>`;
      });
      $('#results').html(html);
    }
  });
});
```

**Characteristics:**
- Manual event handling
- JSON responses
- Client-side rendering
- ~30-60 lines per pattern

### HTMX Approach

```html
<!-- Declarative HTML -->
<input hx-get="/search/"
       hx-trigger="keyup changed delay:300ms"
       hx-target="#results">
<div id="results"></div>
```

```python
# Server returns HTML
def search(request):
    query = request.GET.get('q')
    results = Contact.objects.filter(name__icontains=query)
    return render(request, 'results.html', {'results': results})
```

**Characteristics:**
- Declarative attributes
- HTML responses
- Server-side rendering
- ~10-20 lines per pattern

### Code Reduction

On average, HTMX reduces code by **66%** compared to jQuery/AJAX:

| Pattern | jQuery | HTMX | Reduction |
|---------|--------|------|-----------|
| Forms | 35 lines | 15 lines | 57% |
| Search | 40 lines | 12 lines | 70% |
| Infinite Scroll | 60 lines | 20 lines | 67% |
| Modals | 30 lines | 10 lines | 67% |
| Dynamic Lists | 50 lines | 18 lines | 64% |
| Dropdowns | 55 lines | 25 lines | 55% |
| Polling | 45 lines | 8 lines | 82% |

## Common Patterns Quick Reference

### Form Submission

```html
<form hx-post="/submit/" hx-target="#result">
  {% csrf_token %}
  <input name="email">
  <button type="submit">Submit</button>
</form>
<div id="result"></div>
```

### Live Search

```html
<input hx-get="/search/"
       hx-trigger="keyup changed delay:300ms"
       hx-target="#results">
```

### Infinite Scroll

```html
<div hx-get="/items/?page=2"
     hx-trigger="revealed"
     hx-swap="afterend">
  Loading...
</div>
```

### Delete Item

```html
<button hx-delete="/items/{{ id }}/"
        hx-target="closest .item"
        hx-swap="outerHTML"
        hx-confirm="Are you sure?">
  Delete
</button>
```

### Dependent Dropdowns

```html
<select hx-get="/states/"
        hx-target="#states"
        hx-trigger="change">
</select>
<select id="states"></select>
```

### Polling

```html
<div hx-get="/status/"
     hx-trigger="load, every 5s">
</div>
```

## Testing the Examples

### Manual Testing Checklist

For each pattern, verify:

- [ ] jQuery version works correctly
- [ ] HTMX version works correctly
- [ ] Both produce identical user experience
- [ ] Loading indicators show during requests
- [ ] Errors are handled gracefully
- [ ] Network requests look correct in DevTools
- [ ] No JavaScript console errors

### Automated Testing

Example test:

```python
from django.test import TestCase, Client

class HTMXExamplesTest(TestCase):
    def test_contact_search_htmx(self):
        client = Client()
        response = client.get(
            '/examples/htmx/contacts/search/?q=test',
            HTTP_HX_REQUEST='true'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('contact-item', response.content.decode())
```

## Troubleshooting

### No Sample Data Shows Up

Run the management command:
```bash
python manage.py create_sample_data
```

### HTMX Not Working

1. Check that htmx.js is loaded (look in browser DevTools)
2. Check for JavaScript console errors
3. Enable HTMX logging: `htmx.logAll()` in console
4. Check Network tab for request/response

### CSRF Token Errors

Make sure forms include `{% csrf_token %}`:
```html
<form hx-post="/submit/">
  {% csrf_token %}
  ...
</form>
```

### Styling Issues

Make sure `examples.css` is loaded:
```html
{% load static %}
<link href="{% static 'css/examples.css' %}" rel="stylesheet">
```

## Contributing

To add new examples:

1. Add model (if needed) to `models.py`
2. Create views in `views.py` (both jQuery and HTMX versions)
3. Add URLs in `urls.py`
4. Create templates in `templates/examples/`
5. Update `comparison.html` and `htmx_deep_dive.html`
6. Document in relevant guides

## Additional Resources

- **HTMX Official Docs**: https://htmx.org/docs/
- **HTMX Examples**: https://htmx.org/examples/
- **Django Documentation**: https://docs.djangoproject.com/
- **jQuery Documentation**: https://api.jquery.com/

## License

This example code is provided as part of the htmx-demo project and is intended for educational purposes.

