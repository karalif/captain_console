from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="console-index"),
    path('<int:id>', views.get_console_by_id, name="console_details"),
    path('create_console', views.create_console, name="create_console"),
    path('delete_console/<int:id>', views.delete_console, name="delete_console"),
    path('update_console/<int:id>', views.update_console, name="update_console")
]
