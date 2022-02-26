from django.urls import path
from . import views
#urls and routes that determines the progression and redirection of pages
#it is also responsible for linking urls to functions in the views.py page to determine each pages functionality
urlpatterns = [
    path('main', views.index),#root_page,
    path('hassan',views.hassan)]
