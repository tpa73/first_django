from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]
Nums = {}
i = -1
for item in items:
    i += 1
    Nums[item["id"]] = i



def home(request):
    #text = """
    #<h1>Learning Django...</h1
    #<strong>Author</strong>
    #"""
    context = {
        "name":"Петров ИИ",
        "email":"hgh@hohjlkh.ru"
    }
    return render(request, "index.html", context)

def abibas(request):
    text = """
    <h1>Learning Django...</h1
    """
    text = text + "\n" + "<h2>" + str(items[0]["id"]) + " " + items[0]["name"] + " " + str(items[0]["quantity"]) + "</h2>"
    return(HttpResponse(text))

def about(request, num):
    text = """
    <h1>Learning Django...</h1
    """
    if num not in Nums:
        text = "<h1>Item is not in list</h1>"
    else:
        text = text + "\n" + "<h2>" + str(items[Nums[num]]["id"]) + " " + items[Nums[num]]["name"] + " " + str(items[Nums[num]]["quantity"]) + "</h2>"
    return(HttpResponse(text))

def items_list(request):
    
    text = """
    <h1>Learning Django...</h1
    """
    for item in items:
        text = text + "<h2>" + str(item) + "</h2><br>"
    text = text + "<br><br>"
    text = text.replace("\'", "")
 
    for item in items:
        text = text + '<a href="' + str(item["id"]) + '">' + item["name"] + "</a><br>"

    return(HttpResponse(text))