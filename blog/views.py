from django.shortcuts import render, get_object_or_404, reverse  # added reverse with httpResponceRedirect
from django.views import generic, View
from django.http import HttpResponseRedirect
# redirects to postdetail page to see the liked results.
from .models import Post
from .forms import CommentForm


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
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        # if user does not like post, post is always False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            # if user likes post, post is set to True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                # User comment is False until approved by admin
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # if user likes post, post is set to True

        comment_form = CommentForm(data=request.POST)
        # getting the data from the form.

        # If Comment form is valid (all form fields are completed)
        # This below is to process the Comment form.
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
            # else return an empty comment form if mot valid!

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                # commented = true, tells the user
                # their comment is waiting approval!
                "comment_form": comment_form,
                "liked": liked
            },
        )


# the view is for the user to toggle and like a comment
class Postlike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id-request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        # the argument is slug. so that we know what post to load.
        # so now when the user likes or unlikes a post, it will reoload the
        # page and show a like if added!
