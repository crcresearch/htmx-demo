# HTMX Gotchas & Common Pitfalls

## Table of Contents

1. [Mindset Shifts](#mindset-shifts)
2. [Common Mistakes](#common-mistakes)
3. [Django-Specific Issues](#django-specific-issues)
4. [Performance Pitfalls](#performance-pitfalls)
5. [Debugging Challenges](#debugging-challenges)
6. [Best Practices to Avoid Issues](#best-practices-to-avoid-issues)

## Mindset Shifts

### 1. JSON vs HTML

**❌ Wrong Mindset (jQuery):**
```python
# Returning JSON
def get_users(request):
    users = User.objects.all()
    data = [{'id': u.id, 'name': u.name} for u in users]
    return JsonResponse({'users': data})
```

**✅ Correct Mindset (HTMX):**
```python
# Returning HTML
def get_users(request):
    users = User.objects.all()
    return render(request, 'partials/users.html', {'users': users})
```

**Why It Matters:**
- HTMX expects HTML responses, not JSON
- If you return JSON, nothing will happen (no errors, just nothing)
- This is the #1 mistake when transitioning from jQuery

### 2. Client-Side State vs Server-Side State

**❌ Wrong Mindset:**
```javascript
// Trying to maintain state in JavaScript
let selectedItems = [];

function addItem(id) {
    selectedItems.push(id);
    updateUI();
}
```

**✅ Correct Mindset:**
```python
# State lives on the server (or in the DOM)
def add_item(request):
    item_id = request.POST.get('item_id')
    # Add to session or database
    request.session.setdefault('selected_items', []).append(item_id)
    return render(request, 'partials/selected_items.html', {
        'items': request.session['selected_items']
    })
```

**Why It Matters:**
- HTMX encourages server-side state management
- Client-side state should be minimal (in DOM attributes if needed)
- This reduces complexity and synchronization issues

### 3. Thinking in Components vs Hypermedia

**❌ Wrong Mindset:**
```javascript
// Thinking like a SPA
class UserList extends React.Component {
    // Complex component logic
}
```

**✅ Correct Mindset:**
```html
<!-- Thinking in hypermedia exchanges -->
<div hx-get="/users" hx-trigger="load">
    <!-- Server sends the complete HTML -->
</div>
```

**Why It Matters:**
- HTMX isn't a component framework
- Think about server exchanges, not component lifecycle
- Focus on request/response, not component state

## Common Mistakes

### 1. Forgetting CSRF Tokens

**❌ Problem:**
```html
<form hx-post="/submit/">
    <!-- Missing CSRF token! -->
    <input name="email">
    <button type="submit">Submit</button>
</form>
```

**Result:** POST requests fail with 403 Forbidden

**✅ Solution:**
```html
<form hx-post="/submit/">
    {% csrf_token %}
    <input name="email">
    <button type="submit">Submit</button>
</form>
```

**Alternative for Non-Form Requests:**
```html
<button hx-post="/api/action/"
        hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>
    Action
</button>
```

### 2. Wrong HTTP Status Codes

**❌ Problem:**
```python
def submit_form(request):
    if errors:
        # Returns error HTML but with 200 status
        return render(request, 'errors.html', {'errors': errors})
```

**Result:** HTMX treats it as success; errors don't trigger error events

**✅ Solution:**
```python
def submit_form(request):
    if errors:
        # Return appropriate status code
        return render(request, 'errors.html', 
                     {'errors': errors}, 
                     status=400)
```

**Status Code Guidelines:**
- `200`: Success
- `400`: Validation errors
- `404`: Not found
- `500`: Server error
- `204`: Success with no content (empty response)

### 3. Incorrect Target Selectors

**❌ Problem:**
```html
<button hx-get="/data" hx-target="results">
    <!-- Missing # for ID selector! -->
    Load
</button>
<div id="results"></div>
```

**Result:** Nothing happens; HTMX can't find the target

**✅ Solution:**
```html
<button hx-get="/data" hx-target="#results">
    Load
</button>
<div id="results"></div>
```

**Selector Options:**
- `#id`: Target by ID
- `.class`: Target by class (first match)
- `this`: Target the element itself
- `closest .class`: Find nearest parent with class
- `next .class`: Next sibling with class
- `previous .class`: Previous sibling with class

### 4. Missing `name` Attributes

**❌ Problem:**
```html
<form hx-post="/submit/">
    {% csrf_token %}
    <input type="text" id="email">
    <!-- Missing name attribute! -->
    <button type="submit">Submit</button>
</form>
```

**Result:** Form data not sent to server

**✅ Solution:**
```html
<form hx-post="/submit/">
    {% csrf_token %}
    <input type="text" id="email" name="email">
    <button type="submit">Submit</button>
</form>
```

**Why It Matters:**
- HTMX serializes form data using `name` attributes
- IDs alone are not enough
- This is standard HTML behavior, but easy to forget

### 5. Incorrect Swap Strategy

**❌ Problem:**
```html
<!-- Want to add item to list -->
<button hx-get="/new-item" 
        hx-target="#item-list"
        hx-swap="innerHTML">
    Add Item
</button>
```

**Result:** Replaces entire list with just the new item

**✅ Solution:**
```html
<button hx-get="/new-item" 
        hx-target="#item-list"
        hx-swap="beforeend">
    <!-- Appends new item to list -->
    Add Item
</button>
```

**Swap Options:**
- `innerHTML`: Replace contents (default)
- `outerHTML`: Replace element itself
- `beforebegin`: Before the element
- `afterbegin`: As first child
- `beforeend`: As last child (append)
- `afterend`: After the element
- `delete`: Remove the target
- `none`: Don't swap (useful for side effects)

### 6. Not Handling Empty Responses

**❌ Problem:**
```python
def delete_item(request, item_id):
    Item.objects.get(id=item_id).delete()
    return HttpResponse('')  # Empty response
```

```html
<button hx-delete="/items/{{ item.id }}/"
        hx-target="#item-{{ item.id }}">
    Delete
</button>
```

**Result:** Item still visible (empty string is swapped in with innerHTML)

**✅ Solution:**
```html
<button hx-delete="/items/{{ item.id }}/"
        hx-target="#item-{{ item.id }}"
        hx-swap="outerHTML">
    <!-- outerHTML removes the element when response is empty -->
    Delete
</button>
```

**Alternative:**
```html
<button hx-delete="/items/{{ item.id }}/"
        hx-target="#item-{{ item.id }}"
        hx-swap="delete">
    Delete
</button>
```

### 7. Trigger Timing Issues

**❌ Problem:**
```html
<!-- Triggers on every keypress -->
<input hx-get="/search" hx-trigger="keyup">
```

**Result:** Excessive server requests; poor performance

**✅ Solution:**
```html
<!-- Debounce with delay -->
<input hx-get="/search" 
       hx-trigger="keyup changed delay:300ms">
```

**Trigger Modifiers:**
- `delay:Xms`: Debounce
- `throttle:Xms`: Rate limit
- `changed`: Only if value changed
- `once`: Only fire once
- `consume`: Prevent default

### 8. Not Using Indicators

**❌ Problem:**
```html
<button hx-get="/slow-endpoint">
    Load Data
</button>
```

**Result:** No feedback during loading; poor UX

**✅ Solution:**
```html
<button hx-get="/slow-endpoint">
    Load Data
    <span class="htmx-indicator">⏳</span>
</button>

<style>
    .htmx-indicator {
        display: none;
    }
    .htmx-request .htmx-indicator {
        display: inline;
    }
</style>
```

**Or with separate indicator:**
```html
<button hx-get="/slow-endpoint" hx-indicator="#spinner">
    Load Data
</button>
<span id="spinner" class="htmx-indicator">Loading...</span>
```

## Django-Specific Issues

### 1. Middleware Issues

**Problem:** Custom middleware that redirects or modifies responses can interfere with HTMX requests.

**Solution:** Check for HTMX requests in middleware:
```python
def my_middleware(get_response):
    def middleware(request):
        # Check if it's an HTMX request
        if request.headers.get('HX-Request'):
            # Handle HTMX requests differently
            pass
        
        response = get_response(request)
        return response
    return middleware
```

### 2. Template Fragment Duplication

**❌ Problem:**
```html
<!-- full_page.html -->
<div class="users">
    {% for user in users %}
        <div>{{ user.name }}</div>
    {% endfor %}
</div>

<!-- partials/users.html (duplicate logic) -->
{% for user in users %}
    <div>{{ user.name }}</div>
{% endfor %}
```

**✅ Solution:** Use template includes
```html
<!-- full_page.html -->
<div class="users">
    {% include "partials/user_list.html" %}
</div>

<!-- partials/users.html (HTMX response) -->
{% include "partials/user_list.html" %}

<!-- partials/user_list.html (shared) -->
{% for user in users %}
    <div>{{ user.name }}</div>
{% endfor %}
```

### 3. URL Reverse Issues

**❌ Problem:**
```html
<button hx-post="/examples/tasks/{{ task.id }}/delete/">
    Delete
</button>
```

**Result:** Brittle; breaks if URL structure changes

**✅ Solution:**
```html
<button hx-post="{% url 'examples:task_delete_htmx' task.id %}">
    Delete
</button>
```

### 4. Missing `request.htmx` Detection

**Problem:** Not distinguishing between full page and HTMX requests

**Solution:** Use django-htmx or check headers
```python
# Install: pip install django-htmx

# Check in view
def my_view(request):
    if request.htmx:
        # Return partial
        return render(request, 'partials/content.html')
    else:
        # Return full page
        return render(request, 'full_page.html')
```

**Manual check:**
```python
def my_view(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
```

## Performance Pitfalls

### 1. Returning Too Much HTML

**❌ Problem:**
```python
def update_item(request, item_id):
    # Returns entire page worth of HTML
    items = Item.objects.all()  # 1000+ items
    return render(request, 'all_items.html', {'items': items})
```

**Result:** Slow responses; large payload

**✅ Solution:**
```python
def update_item(request, item_id):
    # Return only the updated item
    item = Item.objects.get(id=item_id)
    return render(request, 'partials/item.html', {'item': item})
```

### 2. N+1 Queries

**❌ Problem:**
```python
def get_users(request):
    users = User.objects.all()  # Query 1
    # Template loops and accesses user.profile (Query 2, 3, 4...)
    return render(request, 'users.html', {'users': users})
```

**✅ Solution:**
```python
def get_users(request):
    users = User.objects.select_related('profile').all()
    return render(request, 'users.html', {'users': users})
```

### 3. No Pagination

**❌ Problem:**
```html
<div hx-get="/all-items" hx-trigger="load">
    <!-- Returns 10,000 items at once -->
</div>
```

**✅ Solution:**
```python
from django.core.paginator import Paginator

def get_items(request):
    page = request.GET.get('page', 1)
    items = Item.objects.all()
    paginator = Paginator(items, 20)
    return render(request, 'items.html', {
        'items': paginator.get_page(page),
        'page_obj': paginator.get_page(page)
    })
```

### 4. Excessive Polling

**❌ Problem:**
```html
<!-- Polls every second -->
<div hx-get="/status" hx-trigger="every 1s"></div>
```

**Result:** Excessive server load

**✅ Solution:**
```html
<!-- Reasonable polling interval -->
<div hx-get="/status" hx-trigger="every 5s"></div>

<!-- Or use Server-Sent Events (SSE) -->
<div hx-ext="sse" sse-connect="/status-stream">
```

## Debugging Challenges

### 1. Silent Failures

**Problem:** HTMX errors don't always show up in console

**Solution:** Enable logging
```javascript
// In browser console or script tag
htmx.logAll();
```

**Add global event listeners:**
```javascript
document.body.addEventListener('htmx:responseError', function(evt) {
    console.error('HTMX Error:', evt.detail);
    alert('An error occurred: ' + evt.detail.xhr.status);
});
```

### 2. Can't See Response in DevTools

**Problem:** Need to see what HTML the server returned

**Solution:**
1. Open DevTools Network tab
2. Find the request
3. Click on it
4. View "Response" tab

**Or add response logging:**
```javascript
document.body.addEventListener('htmx:afterRequest', function(evt) {
    console.log('Response:', evt.detail.xhr.responseText);
});
```

### 3. Target Not Found

**Problem:** Element not found by selector

**Solution:** Add debug events
```javascript
document.body.addEventListener('htmx:targetError', function(evt) {
    console.error('Target not found:', evt.detail);
});
```

### 4. CORS Issues in Development

**Problem:** Making requests to different ports/domains

**Solution:** Configure Django CORS
```python
# Install: pip install django-cors-headers

INSTALLED_APPS = [
    'corsheaders',
    # ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

# Development only!
CORS_ALLOW_ALL_ORIGINS = True
```

## Best Practices to Avoid Issues

### 1. Always Use Template Fragments

Create reusable partial templates:
```
templates/
  ├── pages/
  │   └── users.html
  └── partials/
      ├── user_list.html
      ├── user_item.html
      └── user_form.html
```

### 2. Consistent Naming Conventions

```html
<!-- Pattern: {entity}_{action}_{tech} -->

<!-- jQuery endpoints -->
/api/users/search/     → users_search_ajax
/api/users/1/          → user_detail_ajax

<!-- HTMX endpoints -->
/htmx/users/search/    → users_search_htmx
/htmx/users/1/         → user_detail_htmx
```

### 3. Test Both Full Page and HTMX

```python
class MyViewTests(TestCase):
    def test_full_page_request(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'full_page.html')
    
    def test_htmx_request(self):
        response = self.client.get('/users/', 
                                  HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/users.html')
```

### 4. Use Response Headers for Special Cases

```python
def my_view(request):
    response = render(request, 'partial.html')
    
    # Trigger client-side event
    response['HX-Trigger'] = 'itemUpdated'
    
    # Redirect after action
    response['HX-Redirect'] = '/success/'
    
    # Replace URL in browser
    response['HX-Replace-Url'] = '/new-url'
    
    return response
```

### 5. Document Your HTMX Patterns

```html
<!-- 
    PATTERN: Infinite Scroll
    TRIGGER: revealed
    TARGET: self (outerHTML)
    ENDPOINT: /products/?page=N
    SERVER: Returns products + next trigger
-->
<div hx-get="/products/?page=2"
     hx-trigger="revealed"
     hx-swap="outerHTML">
    Loading...
</div>
```

### 6. Progressive Enhancement

```html
<!-- Works without JavaScript -->
<form action="/submit/" method="post" 
      hx-post="/submit/" 
      hx-target="#result">
    {% csrf_token %}
    <input name="email" type="email" required>
    <button type="submit">Submit</button>
</form>
```

### 7. Graceful Error Handling

```python
def my_view(request):
    try:
        # Your logic here
        return render(request, 'success.html')
    except ValidationError as e:
        return render(request, 'error.html', 
                     {'error': str(e)}, status=400)
    except Exception as e:
        logger.error(f"Error in my_view: {e}")
        return render(request, 'error.html', 
                     {'error': 'An unexpected error occurred'}, 
                     status=500)
```

## Checklist for Debugging HTMX Issues

- [ ] Is `htmx.js` loaded? Check network tab
- [ ] Is the endpoint returning HTML, not JSON?
- [ ] Is the HTTP status code correct?
- [ ] Is the CSRF token included (for POST/PUT/DELETE)?
- [ ] Is the target selector correct? (Don't forget `#` for IDs)
- [ ] Do form fields have `name` attributes?
- [ ] Is the swap strategy appropriate?
- [ ] Are you using the right HTTP method?
- [ ] Check browser console for errors
- [ ] Check network tab for request/response
- [ ] Try `htmx.logAll()` in console
- [ ] Are there any middleware interfering?
- [ ] Is the response being cached inappropriately?

## Summary

The key to avoiding HTMX gotchas is remembering:

1. **Return HTML, not JSON**
2. **Use correct status codes**
3. **Include CSRF tokens**
4. **Use proper selectors**
5. **Add name attributes to form fields**
6. **Choose appropriate swap strategies**
7. **Handle loading states**
8. **Keep responses small**
9. **Test thoroughly**
10. **Enable logging during development**

Most issues stem from thinking in jQuery/SPA patterns rather than hypermedia patterns. Once you internalize "server returns HTML" and "state lives on server," most problems disappear.

