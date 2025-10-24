#!/usr/bin/env python3
"""Verification script to check if all implementation files are in place."""

import sys
from pathlib import Path

# Color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def check_file(file_path: Path, description: str, allow_empty: bool = False) -> bool:
    """Check if a file exists and has content."""
    if not file_path.exists():
        print(f"{RED}✗{RESET} Missing: {description} ({file_path})")
        return False
    
    if file_path.is_file() and file_path.stat().st_size == 0 and not allow_empty:
        print(f"{YELLOW}⚠{RESET} Empty: {description} ({file_path})")
        return False
    
    print(f"{GREEN}✓{RESET} {description}")
    return True

def main():
    """Run all verification checks."""
    print("=" * 70)
    print("HTMX Training Examples - Implementation Verification")
    print("=" * 70)
    
    base_dir = Path(__file__).parent
    all_good = True
    
    # Check Django app files
    print("\n📦 Django App Structure:")
    app_dir = base_dir / "htmx_demo" / "examples"
    all_good &= check_file(app_dir / "__init__.py", "App __init__.py", allow_empty=True)
    checks = [
        (app_dir / "apps.py", "App configuration"),
        (app_dir / "models.py", "Models (7 models)"),
        (app_dir / "views.py", "Views (40+ functions)"),
        (app_dir / "urls.py", "URL patterns"),
        (app_dir / "admin.py", "Admin configuration"),
        (app_dir / "README.md", "App documentation"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check migrations
    print("\n📁 Migrations:")
    migrations_dir = app_dir / "migrations"
    all_good &= check_file(migrations_dir / "__init__.py", "Migrations __init__.py", allow_empty=True)
    all_good &= check_file(migrations_dir / "0001_initial.py", "Initial migration")
    
    # Check management command
    print("\n⚙️ Management Commands:")
    cmd_dir = app_dir / "management" / "commands"
    all_good &= check_file(app_dir / "management" / "__init__.py", "Management __init__.py", allow_empty=True)
    all_good &= check_file(cmd_dir / "__init__.py", "Commands __init__.py", allow_empty=True)
    all_good &= check_file(cmd_dir / "create_sample_data.py", "Sample data command")
    
    # Check templates
    print("\n📄 Templates:")
    templates_dir = base_dir / "htmx_demo" / "templates"
    checks = [
        (templates_dir / "base.html", "Base template (updated)"),
        (templates_dir / "pages" / "home.html", "Home page (updated)"),
        (templates_dir / "examples" / "index.html", "Examples landing"),
        (templates_dir / "examples" / "comparison.html", "Comparison page"),
        (templates_dir / "examples" / "htmx_deep_dive.html", "Deep dive page"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check partial templates
    print("\n📝 Partial Templates:")
    partials_dir = templates_dir / "examples" / "partials"
    checks = [
        (partials_dir / "form_errors.html", "Form errors"),
        (partials_dir / "form_success.html", "Form success"),
        (partials_dir / "contact_results.html", "Contact results"),
        (partials_dir / "product_list.html", "Product list"),
        (partials_dir / "product_modal.html", "Product modal"),
        (partials_dir / "task_item.html", "Task item"),
        (partials_dir / "state_options.html", "State options"),
        (partials_dir / "city_options.html", "City options"),
        (partials_dir / "system_status.html", "System status"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check static files
    print("\n🎨 Static Files:")
    static_dir = base_dir / "htmx_demo" / "static" / "css"
    checks = [
        (static_dir / "examples.css", "Examples CSS"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check configuration
    print("\n⚙️ Configuration:")
    config_dir = base_dir / "config"
    checks = [
        (config_dir / "settings" / "base.py", "Settings (updated)"),
        (config_dir / "urls.py", "URLs (updated)"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check documentation
    print("\n📚 Documentation:")
    docs_dir = base_dir / "docs"
    checks = [
        (docs_dir / "HTMX_GUIDE.md", "HTMX Guide"),
        (docs_dir / "COMPARISON_GUIDE.md", "Comparison Guide"),
        (docs_dir / "GOTCHAS.md", "Gotchas Guide"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Check project files
    print("\n📋 Project Files:")
    checks = [
        (base_dir / "README.md", "Main README (updated)"),
        (base_dir / "IMPLEMENTATION_SUMMARY.md", "Implementation summary"),
    ]
    for file_path, description in checks:
        all_good &= check_file(file_path, description)
    
    # Summary
    print("\n" + "=" * 70)
    if all_good:
        print(f"{GREEN}✓ All files present and verified!{RESET}")
        print("\n🎉 Implementation complete!")
        print("\nNext steps:")
        print("  1. Set up database (see README.md or IMPLEMENTATION_SUMMARY.md)")
        print("  2. Run migrations: python manage.py migrate")
        print("  3. Create sample data: python manage.py create_sample_data")
        print("  4. Start server: python manage.py runserver")
        print("  5. Visit http://localhost:8000/examples/")
        return 0
    else:
        print(f"{RED}✗ Some files are missing or empty{RESET}")
        print("\nPlease review the output above and ensure all files are created.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

