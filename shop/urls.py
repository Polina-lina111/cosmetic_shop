from django.urls import path

from .views import (
    home_view,
    product_view,
    search_view,
    shop_redirect_view,
)

urlpatterns = [
    path("", home_view, name="home"),

    path("product/<int:product_id>/", product_view, name="product"),

    path("search/", search_view, name="search"),

    path("shop/", shop_redirect_view, name="shop_redirect"),
]