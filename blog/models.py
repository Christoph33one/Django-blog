from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # Adding a character field for mxax 200 characters
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    # this above creates a table like structure for the admin user.

    class Meta:
        ordering = ["-created_on"]
        # A good idea to use the __str__ method. It returns a string
        # representation of an object.

    def __str__(self):
        return self.title
        # returns the title name

    def number_of_likes(self):
        return self.likes.count()
        # returns how manys likes


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        # returns date of created comment

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
        # returns comment content and name
