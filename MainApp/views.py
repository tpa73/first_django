from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def home(request):
    context = {
        "name": "Петров Peter Николаевич",
        "email": "fdhjgf@gisgia.ru",
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    context = {
        "author": author
    }
    return render(request, "about.html", context)


def get_item(request, item_id: int):
    """ Get item by id from db."""
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {"errors": [f'Item with id={item_id} not found.']}, status=404)
    else:
        color_list = []
        for col in item.colors.all():
            color_list.append(col.name)
        context = {"item": item, "colors":color_list}
        return render(request, "item_page.html", context)
    

def get_items(request):
    """ Get all items from db."""
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)