from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_index, name="product-home_index"),
    path('games/', views.game_index,name="product-game_index"),
    path('consoles/', views.console_index,name="product-console_index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product/<int:id>',views.delete_product, name="delete_product"),
    path('update_product/<int:id>',views.update_product, name="update_product"),

]