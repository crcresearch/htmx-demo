# HTMX Comprehensive Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Essential Attributes](#essential-attributes)
4. [Common Patterns](#common-patterns)
5. [Advanced Features](#advanced-features)
6. [Best Practices](#best-practices)
7. [Debugging](#debugging)

## Introduction

HTMX is a library that allows you to access modern browser features directly from HTML, rather than using JavaScript. It extends HTML with attributes that enable you to:

- Issue AJAX requests directly from HTML elements
- Update parts of the page without full page reloads
- Use CSS transitions for smooth UI updates
- Implement WebSockets and Server-Sent Events
- And much more, all without writing JavaScript

### Philosophy

HTMX follows a "hypermedia-driven" approach:
- **Server returns HTML**, not JSON
- **Less JavaScript** in your codebase
- **Declarative** rather than imperative
- **Progressive enhancement** - it works without JavaScript, but is better with it

## Core Concepts

### Hypermedia as the Engine of Application State (HATEOAS)

Instead of the client managing application state and rendering logic, the server sends HTML that represents the current state. The client (HTMX) simply renders what the server sends.

**Traditional AJAX/jQuery:**
```javascript
// Client-side rendering
$.ajax({
  url: '/api/users',
  success: function(data) {
    let html = '';
    data.users.forEach(user => {
      html += `<div>${user.name}</div>`;
    });
    $('#users').html(html);
  }
});
```

**HTMX:**
```html
<!-- Server-side rendering -->
<button hx-get="/users" hx-target="#users">Load Users</button>
<div id="users"></div>

<!-- Server returns:
<div>John Doe</div>
<div>Jane Smith</div>
-->
```

### Request/Response Cycle

1. User interacts with an element (click, type, etc.)
2. HTMX sends an HTTP request to the server
3. Server processes request and returns HTML
4. HTMX swaps the HTML into the DOM based on your configuration

## Essential Attributes

### Request Attributes

#### `hx-get`, `hx-post`, `hx-put`, `hx-patch`, `hx-delete`

Specify the URL and HTTP method for the request.

```html
<button hx-get="/api/data">Get Data</button>
<form hx-post="/api/submit">...</form>
<button hx-delete="/api/item/5">Delete</button>
```

### Targeting Attributes

#### `hx-target`

Specifies where to insert the response. Can be a CSS selector.

```html
<!-- Insert into a specific element -->
<button hx-get="/data" hx-target="#result">Load</button>
<div id="result"></div>

<!-- Special values -->
<button hx-get="/data" hx-target="this">Replace self</button>
<button hx-get="/data" hx-target="closest .card">Target parent</button>
<button hx-get="/data" hx-target="next .result">Target next sibling</button>
```

#### `hx-swap`

Controls how the response is swapped into the target.

```html
<!-- innerHTML (default) - replace inner content -->
<div hx-get="/data" hx-swap="innerHTML"></div>

<!-- outerHTML - replace entire element -->
<div hx-get="/data" hx-swap="outerHTML"></div>

<!-- beforebegin - insert before target -->
<div hx-get="/data" hx-swap="beforebegin"></div>

<!-- afterbegin - insert as first child -->
<div hx-get="/data" hx-swap="afterbegin"></div>

<!-- beforeend - insert as last child -->
<div hx-get="/data" hx-swap="beforeend"></div>

<!-- afterend - insert after target -->
<div hx-get="/data" hx-swap="afterend"></div>

<!-- delete - remove target element -->
<button hx-delete="/item/1" hx-swap="delete"></button>

<!-- none - don't swap, but still fire events -->
<button hx-post="/log" hx-swap="none"></button>
```

### Trigger Attributes

#### `hx-trigger`

Specifies what event triggers the request.

```html
<!-- Click (default for buttons) -->
<button hx-get="/data">Click me</button>

<!-- Change (default for inputs) -->
<input hx-get="/search" hx-trigger="change">

<!-- Keyup with delay (debouncing) -->
<input hx-get="/search" hx-trigger="keyup changed delay:300ms">

<!-- Multiple triggers -->
<div hx-get="/data" hx-trigger="click, customEvent"></div>

<!-- Load on page load -->
<div hx-get="/data" hx-trigger="load"></div>

<!-- Polling -->
<div hx-get="/status" hx-trigger="every 3s"></div>

<!-- Scroll into view -->
<div hx-get="/page-2" hx-trigger="revealed"></div>

<!-- Intersection observer with threshold -->
<div hx-get="/data" hx-trigger="intersect threshold:0.5"></div>
```

#### Trigger Modifiers

```html
<!-- once - only trigger once -->
<button hx-get="/data" hx-trigger="click once">Click Once</button>

<!-- changed - only trigger if value changed -->
<input hx-get="/search" hx-trigger="keyup changed">

<!-- delay - debounce -->
<input hx-get="/search" hx-trigger="keyup delay:500ms">

<!-- throttle - limit frequency -->
<input hx-get="/search" hx-trigger="keyup throttle:1s">

<!-- from - listen to events on other elements -->
<input id="search" />
<button hx-get="/search" hx-trigger="keyup from:#search">Search</button>

<!-- consume - prevent default behavior -->
<form hx-post="/submit" hx-trigger="submit consume">
```

### Indicator Attributes

#### `hx-indicator`

Show a loading indicator during requests.

```html
<button hx-get="/data" hx-indicator="#spinner">
  Load Data
</button>
<span id="spinner" class="htmx-indicator">Loading...</span>

<style>
  .htmx-indicator {
    display: none;
  }
  .htmx-request .htmx-indicator {
    display: inline;
  }
  .htmx-request.htmx-indicator {
    display: inline;
  }
</style>
```

### Additional Request Data

#### `hx-vals`

Add additional values to the request.

```html
<!-- JSON object -->
<button hx-post="/api/save" 
        hx-vals='{"priority": "high"}'>
  Save
</button>

<!-- JavaScript expression (js: prefix) -->
<button hx-post="/api/save"
        hx-vals='js:{timestamp: Date.now()}'>
  Save
</button>
```

#### `hx-params`

Control which parameters are included.

```html
<!-- All parameters (default) -->
<form hx-post="/submit" hx-params="*"></form>

<!-- None -->
<form hx-post="/submit" hx-params="none"></form>

<!-- Specific parameters -->
<form hx-post="/submit" hx-params="name,email"></form>

<!-- All except specific -->
<form hx-post="/submit" hx-params="not password"></form>
```

### Confirmation & Validation

#### `hx-confirm`

Show a confirmation dialog before making the request.

```html
<button hx-delete="/api/item/5" 
        hx-confirm="Are you sure you want to delete this item?">
  Delete
</button>
```

### Other Important Attributes

#### `hx-push-url`

Update the browser's URL bar and history.

```html
<!-- Push the request URL -->
<a hx-get="/page2" hx-push-url="true">Page 2</a>

<!-- Push a custom URL -->
<button hx-get="/api/data" hx-push-url="/data">Load Data</button>
```

#### `hx-select`

Select a subset of the response to swap.

```html
<!-- Only swap the #results div from response -->
<button hx-get="/page" hx-select="#results" hx-target="#content">
  Load
</button>
```

#### `hx-sync`

Control how requests are synchronized.

```html
<!-- Drop all other requests while processing -->
<input hx-get="/search" hx-sync="this:drop">

<!-- Abort existing request and make new one -->
<input hx-get="/search" hx-sync="this:abort">

<!-- Replace existing request -->
<input hx-get="/search" hx-sync="this:replace">

<!-- Queue requests -->
<input hx-get="/search" hx-sync="this:queue">
```

#### `hx-disable`

Disable an element during a request.

```html
<button hx-post="/submit" hx-disable>
  Submit
</button>
```

## Common Patterns

### Form Submission

```html
<form hx-post="/contact" hx-target="#result">
  <input name="email" type="email" required>
  <button type="submit">Submit</button>
</form>
<div id="result"></div>
```

**Django View:**
```python
def contact_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Process...
        return render(request, 'partials/success.html')
```

### Live Search

```html
<input type="text" 
       name="q"
       hx-get="/search"
       hx-trigger="keyup changed delay:300ms"
       hx-target="#results">
<div id="results"></div>
```

### Infinite Scroll

```html
<div id="content">
  <!-- Initial items -->
  <div hx-get="/items?page=2" 
       hx-trigger="revealed" 
       hx-swap="afterend">
    Loading...
  </div>
</div>
```

### Delete with Confirmation

```html
<button hx-delete="/api/item/5"
        hx-target="closest .item"
        hx-swap="outerHTML swap:1s"
        hx-confirm="Delete this item?">
  Delete
</button>
```

### Dependent Dropdowns

```html
<select name="country" 
        hx-get="/states" 
        hx-target="#states">
  <option>Select Country</option>
</select>

<select id="states" name="state">
  <option>Select State</option>
</select>
```

### Polling

```html
<div hx-get="/status" 
     hx-trigger="load, every 5s"
     hx-swap="innerHTML">
  Loading status...
</div>
```

## Advanced Features

### Events

HTMX triggers events throughout the request lifecycle:

```javascript
// Before request is made
document.body.addEventListener('htmx:beforeRequest', function(evt) {
  console.log('About to make request:', evt.detail);
});

// After request completes
document.body.addEventListener('htmx:afterRequest', function(evt) {
  console.log('Request complete:', evt.detail);
});

// After content is swapped
document.body.addEventListener('htmx:afterSwap', function(evt) {
  console.log('Content swapped:', evt.detail);
});

// After settle (CSS transitions complete)
document.body.addEventListener('htmx:afterSettle', function(evt) {
  console.log('Settled:', evt.detail);
});
```

### Response Headers

HTMX recognizes special response headers:

```python
# Django example
response = HttpResponse(html)

# Trigger client-side redirect
response['HX-Redirect'] = '/new-page'

# Trigger full page refresh
response['HX-Refresh'] = 'true'

# Replace URL in browser
response['HX-Replace-Url'] = '/new-url'

# Trigger client-side event
response['HX-Trigger'] = 'myEvent'

# Trigger multiple events with data
import json
response['HX-Trigger'] = json.dumps({
    'showMessage': {'level': 'info', 'message': 'Success!'},
    'updateCart': None
})
```

### Out of Band Swaps

Update multiple parts of the page with one response:

```html
<!-- Response HTML -->
<div id="main-content">
  Updated main content
</div>

<div id="notification" hx-swap-oob="true">
  <div class="alert">Success!</div>
</div>

<div id="cart-count" hx-swap-oob="innerHTML">5</div>
```

### Extensions

HTMX has several official extensions:

- **class-tools**: Manipulate classes
- **debug**: Enhanced debugging
- **json-enc**: Send JSON instead of form-encoded
- **loading-states**: Show loading states
- **method-override**: Use PUT/DELETE where not supported
- **morphdom**: Use morphdom for swapping
- **multi-swap**: Multiple swaps per request
- **path-deps**: Update on path changes
- **preload**: Preload content
- **remove-me**: Remove element after delay
- **response-targets**: Target based on response code
- **restored**: Handle browser back/forward
- **ws**: WebSocket support

## Best Practices

### 1. Return Appropriate Status Codes

```python
# Success
return HttpResponse(html, status=200)

# Validation error
return HttpResponse(error_html, status=400)

# Not found
return HttpResponse(not_found_html, status=404)

# Server error
return HttpResponse(error_html, status=500)
```

### 2. Use Semantic HTML

```html
<!-- Good: Semantic, accessible -->
<form hx-post="/submit">
  <button type="submit">Submit</button>
</form>

<!-- Avoid: Non-semantic -->
<div hx-post="/submit" hx-trigger="click">Submit</div>
```

### 3. Progressive Enhancement

```html
<!-- Works without JavaScript -->
<form action="/submit" method="post" hx-post="/submit" hx-target="#result">
  <button type="submit">Submit</button>
</form>
```

### 4. Use Appropriate HTTP Methods

- **GET**: Read data (should be idempotent)
- **POST**: Create new resource
- **PUT/PATCH**: Update existing resource
- **DELETE**: Remove resource

### 5. Keep Responses Small

Return only the HTML that needs to be updated, not entire pages.

```html
<!-- Good: Small fragment -->
<div class="notification">Message sent!</div>

<!-- Avoid: Entire page -->
```

### 6. Use CSS for Loading States

```css
.htmx-request {
  cursor: wait;
  opacity: 0.7;
}

.htmx-swapping {
  opacity: 0;
  transition: opacity 200ms ease-out;
}
```

### 7. Handle Errors Gracefully

```python
def my_view(request):
    try:
        # Process request
        return render(request, 'success.html')
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)}, status=500)
```

## Debugging

### Enable Logging

```javascript
// In browser console
htmx.logAll();
```

### Common Issues

**Problem: Nothing happens when clicking**
- Check browser console for errors
- Verify the URL is correct
- Ensure CSRF token is included for POST requests
- Check that target element exists

**Problem: Response not showing up**
- Verify server is returning HTML, not JSON
- Check hx-target selector
- Verify hx-swap method
- Look for JavaScript errors

**Problem: Request not including form data**
- Ensure form fields have `name` attributes
- Check hx-params configuration
- Verify request is using correct HTTP method

### Browser DevTools

- **Network tab**: Inspect requests and responses
- **Console**: Check for HTMX logs and errors
- **Elements**: Verify HTMX attributes are present
- **Performance**: Monitor request timing

### Testing

```python
# Django test example
from django.test import Client

def test_htmx_request():
    client = Client()
    response = client.get('/endpoint', 
                         HTTP_HX_REQUEST='true')
    assert response.status_code == 200
    assert 'expected-content' in response.content.decode()
```

## Resources

- **Official Docs**: https://htmx.org/docs/
- **Examples**: https://htmx.org/examples/
- **Discord Community**: https://htmx.org/discord
- **GitHub**: https://github.com/bigskysoftware/htmx

## Conclusion

HTMX allows you to build modern, dynamic web applications with much less JavaScript than traditional approaches. By returning HTML from the server and using declarative attributes, your code becomes simpler, more maintainable, and easier to understand.

The key is to think in terms of hypermedia exchanges rather than client-side rendering. Let the server control what gets displayed, and let HTMX handle the mechanics of getting it there.

