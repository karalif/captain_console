from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_index, name="product-home_index"),
    path('games/', views.get_games,name="product-game_index"),
    path('consoles/', views.get_consoles,name="product-console_index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('games/<int:id>', views.get_product_by_id, name="product_details"),
    path('consoles/<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product/<int:id>',views.delete_product, name="delete_product"),
    path('update_product/<int:id>',views.update_product, name="update_product")
]