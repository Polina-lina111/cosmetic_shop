from django.http import HttpResponse

from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from django.shortcuts import get_object_or_404

from .models import Product, Review
from .forms import ReviewForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer

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

            Review.objects.create(
                username=form.cleaned_data["username"],
                message=form.cleaned_data["message"],
                rating=form.cleaned_data["rating"],
            )

            return render(
                request,
                "shop/review_success.html"
            )

    else:

        form = ReviewForm()

    reviews = Review.objects.all().order_by("-created_at")

    context = {
        "form": form,
        "reviews": reviews,
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


@login_required
def manager_dashboard_view(request):

    profile = request.user.profile

    if profile.role != "manager":
        return HttpResponseForbidden(
            "У вас немає доступу до цієї сторінки"
        )

    products = Product.objects.filter(
        owner=request.user
    )

    context = {
        "products": products,
    }

    return render(
        request,
        "shop/manager_dashboard.html",
        context,
    )

@login_required
def edit_product_view(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if product.owner != request.user:
        return HttpResponseForbidden(
            "Ви не можете редагувати чужий товар"
        )

    return HttpResponse(
        f"Редагування товару: {product.title}"
    )



@api_view(["GET"])
def product_api_view(request):

    products = Product.objects.all()

    serializer = ProductSerializer(
        products,
        many=True
    )

    return Response(serializer.data)