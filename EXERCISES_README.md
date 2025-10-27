# HTMX Exercises App

A lightweight Django app with fun, hands-on HTMX exercise prompts for training research software engineers.

## What's Been Created

### App Structure
- **Location**: `htmx_demo/exercises/`
- **Type**: Static exercise prompts (no database models)
- **Content**: 6 fun, real-world themed exercises

### Features
- No user tracking or databases - pure learning content
- Hardcoded exercises in `views.py` for easy editing
- Beautiful Bootstrap 5 UI with emoji icons
- Difficulty badges (Beginner, Intermediate, Advanced)
- Collapsible hints for each exercise
- Copyable starter code templates
- Links to HTMX documentation

## The 6 Exercises

### Beginner Level

**1. 🍕 Recipe Finder App**
- Combines: Live search + infinite scroll + modal details
- Patterns: `hx-get`, `hx-trigger`, `hx-swap`, `hx-indicator`
- Build a complete recipe search app with debounced search

**2. 🎫 Support Ticket System**
- Combines: Form validation + ticket list + modal views
- Patterns: `hx-post`, `hx-get`, `hx-target`, form validation
- Create a mini help desk with inline validation

### Intermediate Level

**3. 📋 Kanban Task Board**
- Combines: CRUD operations + drag & drop
- Patterns: `hx-post`, `hx-delete`, `hx-patch`, Sortable.js
- Build a Trello-style board with draggable tasks

**4. ✈️ Travel Destination Planner**
- Combines: Cascading dropdowns + dynamic itinerary
- Patterns: `hx-get`, `hx-target`, `hx-include`, `hx-swap`
- Plan trips with dependent location dropdowns

### Advanced Level

**5. 🚨 System Status Dashboard**
- Combines: Auto-polling + real-time updates
- Patterns: `hx-get`, `hx-trigger="every 3s"`, HTMX events
- Monitor services with auto-refreshing dashboard

**6. 👤 User Onboarding Wizard**
- Combines: Multi-step form + file upload
- Patterns: `hx-post`, `hx-get`, `hx-encoding`, validation
- Create smooth 3-step onboarding flow

## How to Use

### Accessing the Exercises
1. Navigate to: `http://localhost:8000/exercises/`
2. Browse exercises by difficulty level
3. Click "Start Exercise" to view details
4. Copy the starter template
5. Build the feature in your codebase!

### Exercise Structure
Each exercise includes:
- **What You'll Build**: Engaging description of the feature
- **HTMX Patterns**: List of patterns to practice
- **Requirements Checklist**: Specific requirements to implement
- **Starter Template**: Copyable HTML to begin with
- **Hints**: Progressive hints in expandable sections
- **Where to Build**: Suggestions on where to implement

## URLs

- **Exercise List**: `/exercises/`
- **Recipe Finder**: `/exercises/recipe-finder/`
- **Support Tickets**: `/exercises/support-tickets/`
- **Kanban Board**: `/exercises/kanban-board/`
- **Travel Planner**: `/exercises/travel-planner/`
- **Status Dashboard**: `/exercises/status-dashboard/`
- **Onboarding Wizard**: `/exercises/onboarding-wizard/`

## Files Created

### Python Files
- `htmx_demo/exercises/__init__.py`
- `htmx_demo/exercises/apps.py`
- `htmx_demo/exercises/views.py` (contains all exercise data)
- `htmx_demo/exercises/urls.py`

### Templates
- `htmx_demo/templates/exercises/index.html` (listing page)
- `htmx_demo/templates/exercises/detail.html` (exercise details)

### Configuration Updates
- Added to `config/settings/base.py` in `LOCAL_APPS`
- Added to `config/urls.py` with namespace `exercises:`
- Added "Exercises" link to navigation menu in `base.html`

## Customization

### Adding New Exercises

Edit `htmx_demo/exercises/views.py` and add to the `EXERCISES` list:

```python
{
    'slug': 'your-exercise',
    'title': '🎯 Your Exercise Title',
    'difficulty': 'Beginner',  # or Intermediate, Advanced
    'category': 'Your Category',
    'description': 'Brief description',
    'what_youll_build': 'Detailed description...',
    'patterns': ['hx-get', 'hx-post', ...],
    'requirements': ['Requirement 1', 'Requirement 2', ...],
    'starter_html': '<!-- Your starter template -->',
    'hints': ['Hint 1', 'Hint 2', ...],
    'where_to_build': 'Implementation suggestions...',
}
```

### Modifying Existing Exercises

Simply edit the exercise dictionaries in `views.py` - no migrations needed!

## Design Philosophy

- **No tracking**: Focus on learning, not completion metrics
- **Hands-on**: Build in real codebase, not isolated playground
- **Fun themes**: Engaging scenarios make learning enjoyable
- **Combined patterns**: Each exercise teaches multiple concepts
- **Starter templates**: Provide structure without giving answers
- **Progressive hints**: Guide without spoiling the solution

## Team Training Workflow

### Suggested Progression

**Week 1: Beginner Exercises**
- Day 1-2: Recipe Finder (search & scroll)
- Day 3-4: Support Tickets (forms & validation)

**Week 2: Intermediate Exercises**
- Day 1-2: Kanban Board (CRUD & drag-drop)
- Day 3-4: Travel Planner (dependent dropdowns)

**Week 3: Advanced Exercises**
- Day 1-2: Status Dashboard (polling)
- Day 3-4: Onboarding Wizard (multi-step forms)

### Code Review Tips
- Have engineers demo their implementations
- Discuss different approaches to the same exercise
- Compare with examples in the examples app
- Identify common patterns across exercises

## Resources

- **HTMX Documentation**: https://htmx.org/docs/
- **HTMX Examples**: https://htmx.org/examples/
- **Examples App**: `/examples/` in this project
- **Side-by-Side Comparisons**: `/examples/comparison/`

## Technical Notes

- Built with Django function-based views
- No models or database required
- Uses existing Bootstrap 5 styling
- Navigation integrated into main menu
- Responsive design for all screen sizes
- Copy-to-clipboard functionality for code

## Success!

Your HTMX exercises app is now live at:
**http://localhost:8000/exercises/**

Happy learning! 🚀

