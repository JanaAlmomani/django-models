from django.contrib import admin
from django.urls import path
from .views import SnacksListView, SnackDetailsView

urlpatterns = [

    path('',SnacksListView.as_view(), name="Snack_List"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snack_detail")

]