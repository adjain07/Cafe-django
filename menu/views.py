from django.shortcuts import render, get_object_or_404

from .models import Category, MenuItem


def menu_list(request):

    categories = Category.objects.all()

    selected_category = request.GET.get('category')

    items = MenuItem.objects.filter(
        is_available=True
    ).select_related('category')

    if selected_category:
        items = items.filter(
            category__id=selected_category
        )

    context = {
        'categories': categories,
        'items': items,
        'selected_category': selected_category,
    }

    return render(
        request,
        'menu/menu.html',
        context
    )


def menu_detail(request, pk):

    item = get_object_or_404(
        MenuItem,
        pk=pk,
        is_available=True
    )

    return render(
        request,
        'menu/menu_detail.html',
        {
            'item': item,
        }
    )