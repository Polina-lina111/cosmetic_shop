from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime

def home_view(request):
    return HttpResponse("Головна сторінка магазину косметики")


def product_view(request, product_id):
    return HttpResponse(f"Сторінка товару з ID: {product_id}")


def search_view(request):
    brand = request.GET.get("brand")

    if brand:
        return HttpResponse(f"Пошук товарів бренду: {brand}")

    return HttpResponse("Бренд не вказаний")


def shop_redirect_view(request):
    return redirect("home")

def detail_view(request, pk):

    product = {
        "id": pk,
        "name": "Face Cream",
        "description": (
            "Hydrating face cream for dry skin "
            "with natural ingredients and vitamins"
        ),
    }

    related_products = [
        "Lipstick",
        "Serum",
        "Face Mask",
    ]

    context = {
        "product": product,
        "related_products": related_products,
        "current_date": datetime.now(),
    }

    return render(
        request,
        "shop/detail.html",
        context,
    )