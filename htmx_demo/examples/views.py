"""Views for the examples app demonstrating jQuery vs HTMX patterns."""

import random
import time
from decimal import Decimal

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import City
from .models import Contact
from .models import Country
from .models import Location
from .models import Product
from .models import State
from .models import SystemStatus
from .models import Task


# Main Pages
# ============================================================================

def index(request):
    """Landing page for examples."""
    return render(request, "examples/index.html")


def comparison(request):
    """Comparison landing page with links to individual patterns."""
    return render(request, "examples/comparison_index.html")


def comparison_form_submissions(request):
    """Form submissions comparison page."""
    return render(request, "examples/patterns/comparison_form_submissions.html")


def comparison_live_search(request):
    """Live search comparison page."""
    return render(request, "examples/patterns/comparison_live_search.html")


def comparison_infinite_scroll(request):
    """Infinite scroll comparison page."""
    return render(request, "examples/patterns/comparison_infinite_scroll.html")


def comparison_modal_dialogs(request):
    """Modal dialogs comparison page."""
    # Get the first product or create one if none exist
    product = Product.objects.first()
    if not product:
        product = Product.objects.create(
            name="Sample Product",
            description="This is a sample product for demonstration.",
            price="29.99",
            category="electronics",
            in_stock=True,
        )
    
    return render(
        request,
        "examples/patterns/comparison_modal_dialogs.html",
        {"product_id": product.id}
    )


def comparison_dynamic_lists(request):
    """Dynamic lists comparison page."""
    return render(request, "examples/patterns/comparison_dynamic_lists.html")


def comparison_dependent_dropdowns(request):
    """Dependent dropdowns comparison page."""
    return render(request, "examples/patterns/comparison_dependent_dropdowns.html")


def comparison_polling(request):
    """Polling/auto-refresh comparison page."""
    return render(request, "examples/patterns/comparison_polling.html")


def comparison_mapbox(request):
    """Leaflet interactive map comparison page."""
    return render(request, "examples/patterns/comparison_mapbox.html")


def htmx_deep_dive(request):
    """HTMX deep dive page with comprehensive examples."""
    # Get initial data for the page
    tasks = Task.objects.all()[:5]
    products = Product.objects.all()[:10]
    contacts = Contact.objects.all()[:10]
    countries = Country.objects.all()

    return render(
        request,
        "examples/htmx_deep_dive.html",
        {
            "tasks": tasks,
            "products": products,
            "contacts": contacts,
            "countries": countries,
        },
    )


# Pattern 1: Form Submissions (jQuery AJAX endpoints)
# ============================================================================

@require_http_methods(["POST"])
def contact_submit_ajax(request):
    """jQuery AJAX endpoint for contact form submission."""
    # Simulate processing delay
    time.sleep(0.3)

    # Get form data
    first_name = request.POST.get("first_name", "").strip()
    last_name = request.POST.get("last_name", "").strip()
    email = request.POST.get("email", "").strip()
    phone = request.POST.get("phone", "").strip()
    company = request.POST.get("company", "").strip()
    message = request.POST.get("message", "").strip()

    # Validate
    errors = {}
    if not first_name:
        errors["first_name"] = "First name is required"
    if not last_name:
        errors["last_name"] = "Last name is required"
    if not email:
        errors["email"] = "Email is required"
    elif "@" not in email:
        errors["email"] = "Please enter a valid email"
    if not message:
        errors["message"] = "Message is required"

    # Check if email already exists
    if email and Contact.objects.filter(email=email).exists():
        errors["email"] = "This email is already registered"

    if errors:
        return JsonResponse({"success": False, "errors": errors}, status=400)

    # Create contact
    contact = Contact.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        company=company,
        message=message,
    )

    return JsonResponse(
        {
            "success": True,
            "message": f"Thank you, {contact.first_name}! We'll be in touch soon.",
            "contact_id": contact.id,
        },
    )


# Pattern 1: Form Submissions (HTMX endpoints)
# ============================================================================

@require_http_methods(["POST"])
def contact_submit_htmx(request):
    """HTMX endpoint for contact form submission."""
    # Get form data
    first_name = request.POST.get("first_name", "").strip()
    last_name = request.POST.get("last_name", "").strip()
    email = request.POST.get("email", "").strip()
    phone = request.POST.get("phone", "").strip()
    company = request.POST.get("company", "").strip()
    message = request.POST.get("message", "").strip()

    # Validate
    errors = {}
    if not first_name:
        errors["first_name"] = "First name is required"
    if not last_name:
        errors["last_name"] = "Last name is required"
    if not email:
        errors["email"] = "Email is required"
    elif "@" not in email:
        errors["email"] = "Please enter a valid email"
    if not message:
        errors["message"] = "Message is required"

    # Check if email already exists
    if email and Contact.objects.filter(email=email).exists():
        errors["email"] = "This email is already registered"

    if errors:
        # Return error messages as HTML
        return render(
            request,
            "examples/partials/form_errors.html",
            {"errors": errors},
            status=400,
        )

    # Create contact
    contact = Contact.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        company=company,
        message=message,
    )

    # Return success message
    return render(
        request,
        "examples/partials/form_success.html",
        {"contact": contact},
    )


# Pattern 2: Live Search/Filtering (jQuery endpoints)
# ============================================================================

def contact_search_ajax(request):
    """jQuery AJAX endpoint for contact search."""
    query = request.GET.get("q", "").strip()

    if not query:
        contacts = Contact.objects.all()[:20]
    else:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
            | Q(company__icontains=query)
        )[:20]

    data = [
        {
            "id": c.id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "company": c.company,
        }
        for c in contacts
    ]

    return JsonResponse({"results": data, "count": len(data)})


# Pattern 2: Live Search/Filtering (HTMX endpoints)
# ============================================================================

def contact_search_htmx(request):
    """HTMX endpoint for contact search."""
    query = request.GET.get("q", "").strip()

    if not query:
        contacts = Contact.objects.all()[:20]
    else:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
            | Q(company__icontains=query)
        )[:20]

    return render(
        request,
        "examples/partials/contact_results.html",
        {"contacts": contacts, "query": query},
    )


# Pattern 3: Infinite Scroll/Lazy Loading (jQuery endpoints)
# ============================================================================

def products_ajax(request):
    """jQuery AJAX endpoint for paginated products."""
    page = int(request.GET.get("page", 1))
    per_page = 10

    products = Product.objects.all()
    paginator = Paginator(products, per_page)
    page_obj = paginator.get_page(page)

    data = {
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "price": str(p.price),
                "category": p.get_category_display(),
                "in_stock": p.in_stock,
            }
            for p in page_obj
        ],
        "has_next": page_obj.has_next(),
        "next_page": page_obj.next_page_number() if page_obj.has_next() else None,
        "total_pages": paginator.num_pages,
    }

    return JsonResponse(data)


# Pattern 3: Infinite Scroll/Lazy Loading (HTMX endpoints)
# ============================================================================

def products_htmx(request):
    """HTMX endpoint for paginated products."""
    page = int(request.GET.get("page", 1))
    per_page = 10

    products = Product.objects.all()
    paginator = Paginator(products, per_page)
    page_obj = paginator.get_page(page)

    return render(
        request,
        "examples/partials/product_list.html",
        {
            "products": page_obj,
            "page_obj": page_obj,
        },
    )


# Pattern 4: Modal Dialogs (jQuery endpoints)
# ============================================================================

@require_http_methods(["GET"])
def product_detail_ajax(request, product_id):
    """jQuery AJAX endpoint for product detail modal."""
    product = get_object_or_404(Product, id=product_id)

    data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "category": product.get_category_display(),
        "in_stock": product.in_stock,
    }

    return JsonResponse(data)


# Pattern 4: Modal Dialogs (HTMX endpoints)
# ============================================================================

@require_http_methods(["GET"])
def product_detail_htmx(request, product_id):
    """HTMX endpoint for product detail modal."""
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "examples/partials/product_modal.html",
        {"product": product},
    )


# Pattern 5: Dynamic List Operations (jQuery endpoints)
# ============================================================================

@require_http_methods(["POST"])
def task_create_ajax(request):
    """jQuery AJAX endpoint for creating a task."""
    title = request.POST.get("title", "").strip()

    if not title:
        return JsonResponse({"success": False, "error": "Title is required"}, status=400)

    task = Task.objects.create(title=title)

    return JsonResponse(
        {
            "success": True,
            "task": {
                "id": task.id,
                "title": task.title,
                "completed": task.completed,
            },
        },
    )


@require_http_methods(["DELETE"])
def task_delete_ajax(request, task_id):
    """jQuery AJAX endpoint for deleting a task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return JsonResponse({"success": True})


@require_http_methods(["POST"])
def task_toggle_ajax(request, task_id):
    """jQuery AJAX endpoint for toggling task completion."""
    task = get_object_or_404(Task, id=task_id)
    task.toggle_complete()

    return JsonResponse(
        {
            "success": True,
            "task": {
                "id": task.id,
                "title": task.title,
                "completed": task.completed,
            },
        },
    )


# Pattern 5: Dynamic List Operations (HTMX endpoints)
# ============================================================================

@require_http_methods(["POST"])
def task_create_htmx(request):
    """HTMX endpoint for creating a task."""
    title = request.POST.get("title", "").strip()

    if not title:
        return HttpResponse(
            '<div class="alert alert-danger">Title is required</div>',
            status=400,
        )

    task = Task.objects.create(title=title)

    # Return the new task HTML
    return render(
        request,
        "examples/partials/task_item.html",
        {"task": task},
    )


@require_http_methods(["DELETE"])
def task_delete_htmx(request, task_id):
    """HTMX endpoint for deleting a task."""
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    # Return empty response - HTMX will remove the element
    return HttpResponse("")


@require_http_methods(["POST"])
def task_toggle_htmx(request, task_id):
    """HTMX endpoint for toggling task completion."""
    task = get_object_or_404(Task, id=task_id)
    task.toggle_complete()

    # Return updated task HTML
    return render(
        request,
        "examples/partials/task_item.html",
        {"task": task},
    )


# Pattern 6: Dependent Dropdowns (jQuery endpoints)
# ============================================================================

def states_ajax(request):
    """jQuery AJAX endpoint for getting states by country."""
    country_id = request.GET.get("country_id")

    if not country_id:
        return JsonResponse({"states": []})

    states = State.objects.filter(country_id=country_id)

    data = {
        "states": [
            {"id": s.id, "name": s.name, "code": s.code}
            for s in states
        ],
    }

    return JsonResponse(data)


def cities_ajax(request):
    """jQuery AJAX endpoint for getting cities by state."""
    state_id = request.GET.get("state_id")

    if not state_id:
        return JsonResponse({"cities": []})

    cities = City.objects.filter(state_id=state_id)

    data = {
        "cities": [
            {"id": c.id, "name": c.name}
            for c in cities
        ],
    }

    return JsonResponse(data)


# Pattern 6: Dependent Dropdowns (HTMX endpoints)
# ============================================================================

def states_htmx(request):
    """HTMX endpoint for getting states by country."""
    country_id = request.GET.get("country_id")

    if not country_id:
        return HttpResponse('<option value="">Select a state</option>')

    states = State.objects.filter(country_id=country_id)

    return render(
        request,
        "examples/partials/state_options.html",
        {"states": states},
    )


def cities_htmx(request):
    """HTMX endpoint for getting cities by state."""
    state_id = request.GET.get("state_id")

    if not state_id:
        return HttpResponse('<option value="">Select a city</option>')

    cities = City.objects.filter(state_id=state_id)

    return render(
        request,
        "examples/partials/city_options.html",
        {"cities": cities},
    )


# Pattern 7: Polling/Auto-refresh (jQuery endpoints)
# ============================================================================

def system_status_ajax(request):
    """jQuery AJAX endpoint for system status polling."""
    # Simulate status changes
    statuses = SystemStatus.objects.all()

    # Randomly update some statuses for demo purposes
    for status in statuses:
        if random.random() < 0.3:  # 30% chance to change
            status.response_time_ms = random.randint(50, 500)
            if random.random() < 0.1:  # 10% chance of issues
                status.status = random.choice(["degraded", "partial_outage"])
            else:
                status.status = "operational"
            status.save()

    data = {
        "statuses": [
            {
                "service_name": s.service_name,
                "status": s.status,
                "response_time_ms": s.response_time_ms,
                "uptime_percentage": str(s.uptime_percentage),
                "message": s.message,
            }
            for s in statuses
        ],
    }

    return JsonResponse(data)


# Pattern 7: Polling/Auto-refresh (HTMX endpoints)
# ============================================================================

def system_status_htmx(request):
    """HTMX endpoint for system status polling."""
    # Simulate status changes
    statuses = SystemStatus.objects.all()

    # Randomly update some statuses for demo purposes
    for status in statuses:
        if random.random() < 0.3:  # 30% chance to change
            status.response_time_ms = random.randint(50, 500)
            if random.random() < 0.1:  # 10% chance of issues
                status.status = random.choice(["degraded", "partial_outage"])
            else:
                status.status = "operational"
            status.save()

    return render(
        request,
        "examples/partials/system_status.html",
        {"statuses": statuses},
    )


# Pattern 8: Interactive Maps (jQuery endpoints)
# ============================================================================

def locations_search_ajax(request):
    """jQuery AJAX endpoint for location search with filters."""
    category = request.GET.get("category", "")
    min_rating = request.GET.get("min_rating", "")
    price_range = request.GET.get("price_range", "")

    locations = Location.objects.all()

    if category:
        locations = locations.filter(category=category)
    if min_rating:
        locations = locations.filter(rating__gte=float(min_rating))
    if price_range:
        locations = locations.filter(price_range=price_range)

    data = {
        "locations": [
            {
                "id": loc.id,
                "name": loc.name,
                "address": loc.address,
                "latitude": float(loc.latitude),
                "longitude": float(loc.longitude),
                "category": loc.category,
                "description": loc.description,
                "rating": float(loc.rating),
                "price_range": loc.price_range,
            }
            for loc in locations
        ],
        "count": locations.count(),
    }

    return JsonResponse(data)


# Pattern 8: Interactive Maps (HTMX endpoints)
# ============================================================================

def locations_search_htmx(request):
    """HTMX endpoint for location search with filters."""
    category = request.GET.get("category", "")
    min_rating = request.GET.get("min_rating", "")
    price_range = request.GET.get("price_range", "")

    locations = Location.objects.all()

    if category:
        locations = locations.filter(category=category)
    if min_rating:
        locations = locations.filter(rating__gte=float(min_rating))
    if price_range:
        locations = locations.filter(price_range=price_range)

    return render(
        request,
        "examples/partials/location_markers.html",
        {"locations": locations},
    )

