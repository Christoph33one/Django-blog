from django.shortcuts import render
from django.views import generic
from .models import Post


# view created. step 1
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html' #  html file to be rendered
    paginate_by = 6
    # means it will only show 6 posts per page,
    # and create new pages for more posts.
    # this can be any number you like.
