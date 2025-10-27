"""Views for the exercises app."""

from django.shortcuts import render
from django.http import Http404


# Hardcoded exercise data
EXERCISES = [
    {
        'slug': 'recipe-finder',
        'title': '🍕 Recipe Finder App',
        'difficulty': 'Beginner',
        'category': 'Search, Scroll & Modal',
        'description': 'Build a recipe search app with live search, infinite scroll results, and detailed recipe modals.',
        'what_youll_build': '''Create a dynamic recipe finder that feels like a modern web app! 
        Users will search for recipes as they type, see results load automatically as they scroll, 
        and click any recipe to view full details in a beautiful modal dialog. No page refreshes needed!''',
        'patterns': ['hx-get', 'hx-trigger', 'hx-target', 'hx-swap', 'hx-indicator'],
        'requirements': [
            'Search input that queries as user types (with 500ms debounce)',
            'Loading spinner while search is in progress',
            'Results display without page refresh',
            'Infinite scroll - load more recipes when reaching bottom',
            'Click recipe to open modal with full details',
            'Modal loads content dynamically via HTMX',
        ],
        'starter_html': '''<!-- Recipe Search Container -->
<div class="container">
    <h1>Recipe Finder</h1>
    
    <!-- Search Input -->
    <div class="mb-3">
        <input type="search" 
               class="form-control" 
               name="q" 
               placeholder="Search recipes...">
        <div class="spinner-border htmx-indicator" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>
    
    <!-- Results Container -->
    <div id="recipe-results">
        <!-- Recipe cards will appear here -->
    </div>
    
    <!-- Infinite Scroll Trigger -->
    <div id="load-more">
        <div class="spinner-border"></div>
    </div>
</div>

<!-- Recipe Modal -->
<div class="modal fade" id="recipeModal">
    <div class="modal-dialog">
        <div class="modal-content" id="modal-content">
            <!-- Modal content loads here -->
        </div>
    </div>
</div>''',
        'hints': [
            'Use hx-get="/api/recipes/search/" on the search input',
            'Add hx-trigger="keyup changed delay:500ms" for debounced search',
            'Use hx-trigger="revealed" on the load-more div for infinite scroll',
            'For modals, use hx-get on the recipe card with data-bs-toggle="modal"',
        ],
        'where_to_build': 'Create a new view in the examples app or build in your own custom app. You\'ll need both backend endpoints (search, load-more, recipe-detail) and frontend templates.',
    },
    {
        'slug': 'support-tickets',
        'title': '🎫 Support Ticket System',
        'difficulty': 'Beginner',
        'category': 'Forms & Validation',
        'description': 'Build a support ticket system with form validation, ticket listing, and modal detail views.',
        'what_youll_build': '''Create a mini help desk system where users can submit support tickets and view them! 
        The form validates in real-time, tickets appear in a list instantly after submission, 
        and clicking any ticket opens a modal with full details and responses. Perfect for learning forms and modals together!''',
        'patterns': ['hx-post', 'hx-get', 'hx-target', 'hx-swap', 'form validation'],
        'requirements': [
            'Submit ticket form with validation (subject, description, priority)',
            'Display validation errors inline without page refresh',
            'Show success message after submission',
            'Clear form after successful submission',
            'Display list of all tickets',
            'Click ticket to view details in modal',
            'Modal shows ticket info and any responses',
        ],
        'starter_html': '''<!-- Support Ticket System -->
<div class="container">
    <h1>Submit a Support Ticket</h1>
    
    <!-- Ticket Form -->
    <form id="ticket-form">
        {% csrf_token %}
        
        <div class="mb-3">
            <label for="subject">Subject</label>
            <input type="text" class="form-control" name="subject" required>
        </div>
        
        <div class="mb-3">
            <label for="description">Description</label>
            <textarea class="form-control" name="description" rows="4" required></textarea>
        </div>
        
        <div class="mb-3">
            <label for="priority">Priority</label>
            <select class="form-select" name="priority">
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select>
        </div>
        
        <button type="submit" class="btn btn-primary">Submit Ticket</button>
    </form>
    
    <!-- Form Result Messages -->
    <div id="form-result" class="mt-3"></div>
    
    <hr class="my-5">
    
    <!-- Tickets List -->
    <h2>Your Tickets</h2>
    <div id="tickets-list">
        <!-- Ticket items will appear here -->
    </div>
</div>

<!-- Ticket Detail Modal -->
<div class="modal fade" id="ticketModal">
    <div class="modal-dialog">
        <div class="modal-content" id="ticket-modal-content">
            <!-- Ticket details load here -->
        </div>
    </div>
</div>''',
        'hints': [
            'Use hx-post="/api/tickets/submit/" on the form',
            'Set hx-target="#form-result" to show validation errors or success',
            'After success, trigger an update to refresh the tickets list',
            'Use hx-get for each ticket card to load details in the modal',
        ],
        'where_to_build': 'Extend the examples app or create a new Django view. You\'ll need endpoints for form submission, ticket listing, and ticket detail.',
    },
    {
        'slug': 'kanban-board',
        'title': '📋 Kanban Task Board',
        'difficulty': 'Intermediate',
        'category': 'CRUD & Drag-Drop',
        'description': 'Build a Kanban board with task CRUD operations and drag-and-drop between columns.',
        'what_youll_build': '''Create your own Trello-style task board! Add tasks that appear instantly, 
        drag them between columns (To Do, In Progress, Done), edit task details inline, and delete tasks 
        with a satisfying animation. This combines HTMX with Sortable.js for the ultimate interactive experience!''',
        'patterns': ['hx-post', 'hx-delete', 'hx-patch', 'hx-swap', 'Sortable.js integration'],
        'requirements': [
            'Three columns: To Do, In Progress, Done',
            'Quick-add form to create tasks (appear instantly in To Do)',
            'Drag tasks between columns with visual feedback',
            'Save column changes to server when dropped',
            'Click task to edit title/description inline',
            'Delete button on each task (with confirmation)',
            'Smooth animations during operations',
        ],
        'starter_html': '''<!-- Kanban Board -->
<div class="container-fluid">
    <h1>My Kanban Board</h1>
    
    <!-- Quick Add Task -->
    <form id="add-task-form" class="mb-4">
        {% csrf_token %}
        <div class="input-group">
            <input type="text" class="form-control" name="title" placeholder="Add a new task...">
            <button type="submit" class="btn btn-primary">Add Task</button>
        </div>
    </form>
    
    <!-- Kanban Columns -->
    <div class="row">
        <!-- To Do Column -->
        <div class="col-md-4">
            <div class="card">
                <div class="card-header bg-secondary text-white">
                    <h5>📝 To Do</h5>
                </div>
                <div class="card-body sortable-column" id="todo-column" data-column="todo">
                    <!-- Tasks will appear here -->
                </div>
            </div>
        </div>
        
        <!-- In Progress Column -->
        <div class="col-md-4">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h5>🚀 In Progress</h5>
                </div>
                <div class="card-body sortable-column" id="progress-column" data-column="progress">
                    <!-- Tasks will appear here -->
                </div>
            </div>
        </div>
        
        <!-- Done Column -->
        <div class="col-md-4">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h5>✅ Done</h5>
                </div>
                <div class="card-body sortable-column" id="done-column" data-column="done">
                    <!-- Tasks will appear here -->
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Include Sortable.js -->
<script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script>''',
        'hints': [
            'Use hx-post to create tasks, hx-target the correct column',
            'Initialize Sortable.js on each .sortable-column element',
            'On drag end, send hx-post with new column and position',
            'Use hx-delete with hx-confirm for task deletion',
            'Consider using hx-swap="outerHTML" for smooth updates',
        ],
        'where_to_build': 'Create a new model (Task) in the examples app with fields for title, description, column, and order. Build views for CRUD operations.',
    },
    {
        'slug': 'travel-planner',
        'title': '✈️ Travel Destination Planner',
        'difficulty': 'Intermediate',
        'category': 'Dynamic Forms',
        'description': 'Build a travel planner with cascading dropdowns and a dynamic itinerary builder.',
        'what_youll_build': '''Plan your dream vacation! Select a country, watch states/regions appear, 
        then pick a city - all dropdowns update automatically. Add destinations to your itinerary, 
        reorder them with drag-and-drop, and see your trip take shape. Perfect for learning dependent 
        dropdowns and dynamic list management!''',
        'patterns': ['hx-get', 'hx-target', 'hx-include', 'hx-swap', 'hx-post'],
        'requirements': [
            'Country dropdown (pre-populated)',
            'State/Region dropdown (loads based on country)',
            'City dropdown (loads based on state)',
            'Button to add selected destination to itinerary',
            'Itinerary list shows all added destinations',
            'Drag to reorder itinerary items',
            'Remove button for each destination',
            'Display total number of destinations',
        ],
        'starter_html': '''<!-- Travel Planner -->
<div class="container">
    <h1>Plan Your Dream Trip</h1>
    
    <div class="row">
        <!-- Destination Selector -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Select Destination</h5>
                </div>
                <div class="card-body">
                    <!-- Country Dropdown -->
                    <div class="mb-3">
                        <label for="country">Country</label>
                        <select class="form-select" name="country" id="country">
                            <option value="">Choose a country...</option>
                            <option value="us">United States</option>
                            <option value="uk">United Kingdom</option>
                            <option value="fr">France</option>
                            <option value="jp">Japan</option>
                        </select>
                    </div>
                    
                    <!-- State Dropdown (loads dynamically) -->
                    <div class="mb-3">
                        <label for="state">State/Region</label>
                        <select class="form-select" name="state" id="state">
                            <option value="">Select country first...</option>
                        </select>
                    </div>
                    
                    <!-- City Dropdown (loads dynamically) -->
                    <div class="mb-3">
                        <label for="city">City</label>
                        <select class="form-select" name="city" id="city">
                            <option value="">Select state first...</option>
                        </select>
                    </div>
                    
                    <button class="btn btn-primary" id="add-destination">
                        Add to Itinerary
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Itinerary -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Your Itinerary <span class="badge bg-secondary" id="destination-count">0</span></h5>
                </div>
                <div class="card-body">
                    <div id="itinerary-list" class="sortable-list">
                        <!-- Destinations will appear here -->
                        <p class="text-muted">No destinations yet. Add some!</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>''',
        'hints': [
            'Use hx-get on country select with hx-target="#state" to load states',
            'Use hx-get on state select with hx-target="#city" to load cities',
            'Add hx-include to send parent dropdown values with each request',
            'Use hx-post to add destinations to the itinerary',
            'Combine with Sortable.js for reordering destinations',
        ],
        'where_to_build': 'Use the existing Country/State/City models in the examples app. Create endpoints for loading dependent dropdowns and managing the itinerary.',
    },
    {
        'slug': 'status-dashboard',
        'title': '🚨 System Status Dashboard',
        'difficulty': 'Advanced',
        'category': 'Real-time Updates',
        'description': 'Build a live system monitoring dashboard with auto-polling and real-time status updates.',
        'what_youll_build': '''Feel like a DevOps engineer! Monitor multiple services (API, Database, Cache) 
        with a dashboard that automatically refreshes every 3 seconds. Services randomly change status 
        (operational, degraded, down) with color-coded indicators. Add pause/resume controls and see 
        the last update timestamp. Perfect for learning polling and real-time updates!''',
        'patterns': ['hx-get', 'hx-trigger="every 3s"', 'hx-swap', 'HTMX events'],
        'requirements': [
            'Display 4-6 service status cards (API, Database, Cache, etc.)',
            'Each card shows: service name, status, response time, uptime %',
            'Color-coded status: green (operational), yellow (degraded), red (down)',
            'Auto-refresh every 3 seconds',
            'Pause/Resume button to control polling',
            'Display "Last updated" timestamp',
            'Smooth transitions when status changes',
            'Backend simulates random status changes',
        ],
        'starter_html': '''<!-- System Status Dashboard -->
<div class="container">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>System Status Dashboard</h1>
        <div>
            <button id="pause-btn" class="btn btn-warning">⏸️ Pause</button>
            <span class="text-muted ms-3">
                Last updated: <span id="last-update">--</span>
            </span>
        </div>
    </div>
    
    <!-- Status Cards Container -->
    <div id="status-container">
        <!-- Initial status cards -->
        <div class="row">
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body">
                        <h5>API Server</h5>
                        <span class="badge bg-success">Operational</span>
                        <p class="mb-0 mt-2">
                            <small>Response: 45ms | Uptime: 99.9%</small>
                        </p>
                    </div>
                </div>
            </div>
            <!-- More service cards... -->
        </div>
    </div>
</div>''',
        'hints': [
            'Use hx-get="/api/status/" with hx-trigger="load, every 3s" on the container',
            'To pause/resume, use htmx.trigger() JavaScript API or swap the hx-trigger attribute',
            'Use htmx:afterSwap event to update the timestamp after each refresh',
            'Backend should randomly change service statuses for demo purposes',
            'Consider using hx-swap="innerHTML transition:true" for smooth updates',
        ],
        'where_to_build': 'Create a new view that returns randomized status data. Use the existing SystemStatus model in examples app or create mock data.',
    },
    {
        'slug': 'onboarding-wizard',
        'title': '👤 User Onboarding Wizard',
        'difficulty': 'Advanced',
        'category': 'Multi-step Forms',
        'description': 'Build a multi-step onboarding wizard with file upload, validation, and progress tracking.',
        'what_youll_build': '''Create a smooth onboarding experience that every app needs! Users progress through 
        three steps: entering basic info, uploading a profile picture with live preview and progress bar, 
        and setting preferences. Each step validates before advancing, there\'s a progress bar showing 
        completion, and users can navigate backward. Perfect for mastering multi-step forms!''',
        'patterns': ['hx-post', 'hx-get', 'hx-swap', 'hx-encoding="multipart/form-data"', 'htmx events'],
        'requirements': [
            'Step 1: Basic Info (name, email) with validation',
            'Step 2: Profile picture upload with preview and progress bar',
            'Step 3: Preferences (newsletter, theme, notifications)',
            'Progress bar showing current step (1/3, 2/3, 3/3)',
            'Validate each step before allowing next',
            'Previous/Next navigation buttons',
            'Final "Complete" button submits everything',
            'Smooth transitions between steps',
        ],
        'starter_html': '''<!-- Onboarding Wizard -->
<div class="container">
    <div class="card">
        <div class="card-header">
            <h3>Welcome! Let's get you set up</h3>
            
            <!-- Progress Bar -->
            <div class="progress mt-3">
                <div class="progress-bar" id="wizard-progress" style="width: 33%">
                    Step 1 of 3
                </div>
            </div>
        </div>
        
        <div class="card-body">
            <!-- Wizard Content Container -->
            <div id="wizard-content">
                <!-- Step 1: Basic Info -->
                <form id="step-1">
                    {% csrf_token %}
                    <h4>Step 1: Basic Information</h4>
                    
                    <div class="mb-3">
                        <label for="name">Full Name</label>
                        <input type="text" class="form-control" name="name" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="email">Email Address</label>
                        <input type="email" class="form-control" name="email" required>
                    </div>
                    
                    <div class="d-flex justify-content-between">
                        <button type="button" class="btn btn-secondary" disabled>Previous</button>
                        <button type="submit" class="btn btn-primary">Next</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>''',
        'hints': [
            'Use hx-post to validate each step before proceeding',
            'On successful validation, return the next step\'s HTML',
            'Use hx-target="#wizard-content" to swap step content',
            'For file upload, use hx-encoding="multipart/form-data"',
            'Track progress in session or hidden inputs',
            'Update progress bar with htmx:afterSwap event',
            'Use hx-get to load previous step with saved data',
        ],
        'where_to_build': 'Create new views for each step validation and progression. Store form data in session between steps until final submission.',
    },
]


def index(request):
    """Display list of all exercises."""
    # Group exercises by difficulty
    exercises_by_difficulty = {
        'Beginner': [ex for ex in EXERCISES if ex['difficulty'] == 'Beginner'],
        'Intermediate': [ex for ex in EXERCISES if ex['difficulty'] == 'Intermediate'],
        'Advanced': [ex for ex in EXERCISES if ex['difficulty'] == 'Advanced'],
    }
    
    context = {
        'exercises_by_difficulty': exercises_by_difficulty,
        'total_count': len(EXERCISES),
    }
    return render(request, 'exercises/index.html', context)


def detail(request, slug):
    """Display full exercise details."""
    # Find exercise by slug
    exercise = None
    for ex in EXERCISES:
        if ex['slug'] == slug:
            exercise = ex
            break
    
    if not exercise:
        raise Http404("Exercise not found")
    
    context = {
        'exercise': exercise,
    }
    return render(request, 'exercises/detail.html', context)

