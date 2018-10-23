from django.urls import path
from project_app.views  import project_views


urlpatterns = [
    path('project_manage/', project_views.project_manage),
    path('add_project/', project_views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('delete_project/<int:pid>/', views.delete_project),
    path('module_manage/', views.delete_project),
]