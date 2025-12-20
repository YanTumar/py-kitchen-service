from django.urls import path
from .views import (index, DishTypeListView,
                    CookListView,
                    DishListView,
                    CookDetailView,
                    CookUpdateView,
                    DishDetailView,
                    DishDeleteView,
                    DishCreateView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
]

app_name = "kitchen"
