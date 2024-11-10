from django.urls import path
from core.views import index, product_list_view, category_list_view,category_product_list__view, vendor_list_view,vendor_detail_view, product_detail_view, tag_list,ajax_add_review,search_view,filter_product,add_to_cart
# from core import *

app_name = "core"

urlpatterns = [

    # Homepage
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("products/<pid>/",  product_detail_view, name="product-detail"),
    
    # category
    path("category/", category_list_view, name="category-list"),
    path("category/<cid>/", category_product_list__view, name="category-product-list"),

    # Vendor
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendors/<vid>/", vendor_detail_view, name="vendor-detail"),
    
    # tags
    path("products/tag/<slug:tag_slug>/", tag_list, name="tags"),

    # Add review
    path("ajax-add-review/<int:pid>/",ajax_add_review , name="ajax-add-review"),
    
    # Homepage
    path("search/", search_view, name="search"),

    # Filter product URL
    path("filter-products/", filter_product, name="filter-product"),

    path("add-to-cart/", add_to_cart, name="add-to-cart"),
]
