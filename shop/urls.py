from django.urls import path

from .views import (
    home_view,
    product_view,
    search_view,
    shop_redirect_view,
    detail_view,
    product_list_view,
    product_detail_view,
)

urlpatterns = [
    path("", home_view, name="home"),

    path("product/<int:product_id>/", product_view, name="product"),

    path("search/", search_view, name="search"),

    path("shop/", shop_redirect_view, name="shop_redirect"),

    path("detail/<int:pk>/", detail_view, name="detail"),

    path("products/", product_list_view, name="product_list"),

    path("products/<int:pk>/", product_detail_view, name="product_detail"),
]