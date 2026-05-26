from django.http import HttpResponse

from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


from .models import Product
from .forms import ReviewForm

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

def product_list_view(request):

    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(
        request,
        "shop/product_list.html",
        context
    )


def product_detail_view(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    context = {
        "product": product
    }

    return render(
        request,
        "shop/product_detail.html",
        context
    )

class AboutPageView(TemplateView):

    template_name = "shop/about.html"


def review_view(request):

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            return render(
                request,
                "shop/review_success.html"
            )

    else:

        form = ReviewForm()

    context = {
        "form": form
    }

    return render(
        request,
        "shop/review_form.html",
        context
    )

@login_required
def profile_view(request):

    return render(
        request,
        "shop/profile.html",
    )