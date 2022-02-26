from django.urls import path
from . import views
#urls and routes that determines the progression and redirection of pages
#it is also responsible for linking urls to functions in the views.py page to determine each pages functionality
urlpatterns = [
    path('main', views.index),#root_page,
    path('hassan',views.hassan),
    path('edit_page',views.show), #render the edit page
    path('edit',views.edit), #update the information for the user
    path('details',views.details), #render the worker details page
    path('join_workers',views.join), #render the worker details page
    path('register_worker',views.register_worker), #registration form for workers
    ]
