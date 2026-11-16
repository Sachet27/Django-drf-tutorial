from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    # path('', views.ProductListAPIView.as_view(), name= 'product_list'),
    path('', views.ProductNormalCrudView.as_view(), name= 'product_list'),

    # path('<int:product_id>/', views.details, name='product_details'),
    # path('<int:product_id>/', views.ProductRetrieveAPIView.as_view(), name='product_details'),

    # path('create/', views.create, name='create_product'),

    # path('create/', views.ProductCreateAPIView.as_view(), name= 'create_product'),

    # path('<int:product_id>/update/', views.ProductUpdateAPIView.as_view(), name='update_product'),

    # path('<int:product_id>/delete/', views.ProductDestroyAPIView.as_view(), name='delete_product'),

    path('<int:product_id>/', views.ProductNormalCrudView.as_view(), name= 'product_operations'),

    path('custom-list/', views.ProductAddListView.as_view(), name= 'custom_list'),

]
