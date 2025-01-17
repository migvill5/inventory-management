from django.urls import path

from .views import (
    CategoryListView,
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,
    create_location,
    create_fabricant,
    create_category,
    delete_product,
    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    LocationListView,
    FabricantListView
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),
    path('create-location/', create_location, name='create-location'),
    path('create-fabricant/', create_fabricant, name='create-fabricant'),
    path('create-category/', create_category, name='create-category'),
    path('delete-product/<int:product_id>',
         delete_product, name='delete-product'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('location-list/', LocationListView.as_view(), name='location-list'),
    path('fabricant-list/', FabricantListView.as_view(), name='fabricant-list'),
    path('category-list/', CategoryListView.as_view(), name='category-list')
]
