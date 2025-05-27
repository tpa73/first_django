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
    #context = {
    #    "name":"Петров ИИ",
    #    "email":"hgh@hohjlkh.ru"
    #}
    #return render(request, "index.html", context)

    # for item in items:
    #     if item["id"] == item_id:
    #         result = f"""
    #         <h2> Имя: {item['name']} </h2>
    #         <br><br>
    #         <p> <a href="/items"> Назад к списку товаров </a></p>
    #         """
     return HttpResponse(result)

def about(request):
#     text = """
#     <h1>Learning Django...</h1
#     """
#     #if num not in Nums:
#     #    text = "<h1>Item is not in list</h1>"
#     #else:
#     #    text = text + "\n" + "<h2>" + str(items[Nums[num]]["id"]) + " " + items[Nums[num]]["name"] + " " + str(items[Nums[num]]["quantity"]) + "</h2>"
    
#     author = {
#         "name":" Пётр",
#         "middle_name":" Иваныч",
#         "last_name":" Сидоров",
#         "phone":" +76465465464",
#         "email":" fjhf@kgkg.ru"
#     }
    
#     context = {"author":author}
    
    return render(request, "about.html", context)

def get_item(request, item_id: int):
    """По указанному id возращает элемент из списка."""
    for item in items:
        if item["id"] == item_id:
            result = f"""
            <h2> Имя: {item['name']} </h2>
            <p> Количество: {item['quantity']}</p>
            <br><br>
            <p> <a href="/items"> Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
    
    return HttpResponseNotFound(f'Item with id={item_id} not found.')


def items_list(request):
    text = """
    <h1>Learning Django...</h1
    """
    #for item in items:
    #    text = text + "<h2>" + str(item) + "</h2><br>"
    #text = text + "<br><br>"
    #text = text.replace("\'", "")
 
    #for item in items:
    #    text = text + '<a href="' + str(item["id"]) + '">' + item["name"] + "</a><br>"

    #return(HttpResponse(text))

    #result = "<h1>Список товаров</h1><ol>"

    #for item in items:
    #    result += f"""<li><a href="/item['id']">{item['name']}</a</<li>"""
    #result += "/ol"
    
    context = {"items": items}

    return render(request, "items_list.html", context)