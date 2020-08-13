from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


# Create your views here.

def index(request):
    allProds = []
    category_of_products = Product.objects.values('category', 'id')
    categories = {item['category'] for item in category_of_products}

    for category in categories:
        product = Product.objects.filter(category=category)
        n = len(product)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search', "")
    print(query)
    allProds = []
    category_of_products = Product.objects.values('category', 'id')
    categories = {item['category'] for item in category_of_products}

    for category in categories:
        productTemp = Product.objects.filter(category=category)
        product = [item for item in productTemp if searchMatch(query, item)]
        n = len(product)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        if len(product) != 0:
            allProds.append([product, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        desc = request.POST.get('desc', "")
        my_contact = Contact(name=name, email=email, phone=phone, desc=desc)
        my_contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': thank})
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('orderId', "")
        email = request.POST.get('email', "")
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timeStamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('[[{}],"{}"]')
        except Exception as e:
            return HttpResponse('[[{}],"{}"]')

    return render(request, 'shop/tracker.html')


def productView(request, myid):
    # fetching product by id
    product = Product.objects.filter(id=myid)
    # print(product)
    params = {'product': product[0]}
    return render(request, 'shop/productView.html', params)


def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        address = request.POST.get('address1', "") + request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip_code = request.POST.get('zip_code', "")
        my_order = Order(name=name, email=email, phone=phone, address=address, city=city, state=state,
                         zip_code=zip_code, items_json=item_json)
        my_order.save()
        update = OrderUpdate(order_id=my_order.order_id, update_desc="Your order has been placed successfully")
        update.save()
        thank = True
        my_id = my_order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': my_id})
    else:
        return render(request, 'shop/checkout.html')
