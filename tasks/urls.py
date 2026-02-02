import uuid

from django.urls import path

from tasks.views import index, id_view, uuid_view

urlpatterns = [
    path('', index),
    path('<num>/',id_view),
    path('<uuid>/',uuid_view),
]