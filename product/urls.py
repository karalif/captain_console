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
    path('update_product/<int:id>',views.update_product, name="update_product"),
    #categories
    path('gameboy/',views.get_gameboy, name="product-gameboy_index"),
    path('gameboy/<int:id>', views.get_product_by_id, name="product_details"),
    path('neo/', views.get_neo, name="product-neo_index"),
    path('neo/<int:id>', views.get_product_by_id, name="product_details"),
    path('nes/', views.get_nes, name="product-nes_index"),
    path('nes/<int:id>', views.get_product_by_id, name="product_details"),
    path('sega/', views.get_sega, name="product-sega_index"),
    path('sega/<int:id>', views.get_product_by_id, name="product_details"),
    path('turbografix/', views.get_turbografix, name="product-turbografix_index"),
    path('turbografix/<int:id>', views.get_product_by_id, name="product_details")

]