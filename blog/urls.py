from . import views
from django.urls import path

# step 2 for adding views.
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
