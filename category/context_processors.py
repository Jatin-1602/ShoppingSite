from .models import Category

def menu_links(request):
    category_names = Category.objects.all()
    return dict(category_names=category_names)