from django.http import HttpResponse
from django.shortcuts import redirect


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
    return redirect("/")