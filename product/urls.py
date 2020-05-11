from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="product-index")
   # path('<int:id>', views.get_game_by_id, name="game_details"),
    #path('create_game', views.create_game, name="create_game"),
    #path('delete_game/<int:id>',views.delete_game, name="delete_game"),
    #path('update_game/<int:id>',views.update_game, name="update_game")
]