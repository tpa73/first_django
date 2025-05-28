"""
URL configuration for FirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf.urls.static import static
from django.conf import settings


#items = [
#   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#   {"id": 7, "name": "Картофель фри" ,"quantity":0},
#   {"id": 8, "name": "Кепка" ,"quantity":124},
#]


# urlpatterns = [
#     path("", views.home),
#     path('item/<int:item_id>', views.get_item, name=),
#     path("items", views.items_list),
#     path("about", views.about, name="ab")
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('item/<int:item_id>', views.get_item, name='item-detail'),
    path('items', views.get_items, name='items-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#    path("5", views.coca),
#    path("7", views.fri),
#    path("8", views.kepka)
#]
