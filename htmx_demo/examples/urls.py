"""URL configuration for the examples app."""

from django.urls import path

from . import views

app_name = "examples"

urlpatterns = [
    # Main pages
    path("", views.index, name="index"),
    path("comparison/", views.comparison, name="comparison"),
    path("comparison/form-submissions/", views.comparison_form_submissions, name="comparison_form_submissions"),
    path("comparison/live-search/", views.comparison_live_search, name="comparison_live_search"),
    path("comparison/infinite-scroll/", views.comparison_infinite_scroll, name="comparison_infinite_scroll"),
    path("comparison/modal-dialogs/", views.comparison_modal_dialogs, name="comparison_modal_dialogs"),
    path("comparison/dynamic-lists/", views.comparison_dynamic_lists, name="comparison_dynamic_lists"),
    path("comparison/dependent-dropdowns/", views.comparison_dependent_dropdowns, name="comparison_dependent_dropdowns"),
    path("comparison/polling/", views.comparison_polling, name="comparison_polling"),
    path("htmx-deep-dive/", views.htmx_deep_dive, name="htmx_deep_dive"),
    # Pattern 1: Form Submissions
    path("api/contact/submit/", views.contact_submit_ajax, name="contact_submit_ajax"),
    path("htmx/contact/submit/", views.contact_submit_htmx, name="contact_submit_htmx"),
    # Pattern 2: Live Search/Filtering
    path("api/contacts/search/", views.contact_search_ajax, name="contact_search_ajax"),
    path("htmx/contacts/search/", views.contact_search_htmx, name="contact_search_htmx"),
    # Pattern 3: Infinite Scroll/Lazy Loading
    path("api/products/", views.products_ajax, name="products_ajax"),
    path("htmx/products/", views.products_htmx, name="products_htmx"),
    # Pattern 4: Modal Dialogs
    path("api/products/<int:product_id>/", views.product_detail_ajax, name="product_detail_ajax"),
    path("htmx/products/<int:product_id>/", views.product_detail_htmx, name="product_detail_htmx"),
    # Pattern 5: Dynamic List Operations
    path("api/tasks/create/", views.task_create_ajax, name="task_create_ajax"),
    path("api/tasks/<int:task_id>/delete/", views.task_delete_ajax, name="task_delete_ajax"),
    path("api/tasks/<int:task_id>/toggle/", views.task_toggle_ajax, name="task_toggle_ajax"),
    path("htmx/tasks/create/", views.task_create_htmx, name="task_create_htmx"),
    path("htmx/tasks/<int:task_id>/delete/", views.task_delete_htmx, name="task_delete_htmx"),
    path("htmx/tasks/<int:task_id>/toggle/", views.task_toggle_htmx, name="task_toggle_htmx"),
    # Pattern 6: Dependent Dropdowns
    path("api/states/", views.states_ajax, name="states_ajax"),
    path("api/cities/", views.cities_ajax, name="cities_ajax"),
    path("htmx/states/", views.states_htmx, name="states_htmx"),
    path("htmx/cities/", views.cities_htmx, name="cities_htmx"),
    # Pattern 7: Polling/Auto-refresh
    path("api/system-status/", views.system_status_ajax, name="system_status_ajax"),
    path("htmx/system-status/", views.system_status_htmx, name="system_status_htmx"),
]

