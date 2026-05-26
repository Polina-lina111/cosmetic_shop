from django.urls import path

from .views import (
    home_view,
    product_view,
    search_view,
    shop_redirect_view,
    product_list_view,
    product_detail_view,
    AboutPageView,
    review_view,
    profile_view,
    manager_dashboard_view,
    edit_product_view,
)

urlpatterns = [
    path("", home_view, name="home"),

    path("product/<int:product_id>/", product_view, name="product"),

    path("search/", search_view, name="search"),

    path("shop/", shop_redirect_view, name="shop_redirect"),

    path("products/", product_list_view, name="product_list"),

    path("products/<int:pk>/", product_detail_view, name="product_detail"),

    path("about/", AboutPageView.as_view(), name="about"),

    path("review/", review_view, name="review"),

    path("profile/", profile_view, name="profile",),

    path("manager-dashboard/", manager_dashboard_view, name="manager_dashboard"),

    path("product/<int:pk>/edit/", edit_product_view, name="edit_product"),
]