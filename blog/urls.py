from . import views
from django.urls import path

# step 3 for adding views (linked up URL).
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
