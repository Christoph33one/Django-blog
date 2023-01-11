from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


# view created. step 1 (add a view)
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'  # html file to be rendered
    paginate_by = 6
    # means it will only show 6 posts per page,
    # and create new pages for more posts.
    # this can be any number you like.


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False  # if user does not like post, post is always False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            # if user likes post, post is set to True

        return render(

            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }

        )
