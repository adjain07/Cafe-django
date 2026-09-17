from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.menu_list,
        name='menu'
    ),

    path(
        '<int:pk>/',
        views.menu_detail,
        name='menu_detail'
    ),

]