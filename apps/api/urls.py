from django.urls import path, include
from .views import *



urlpatterns = [
    #post
    path('post/', Post_views_list.as_view())

]