from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    # gives a prediction on what the user will add to a title or content box (hello world)
    # look when typing in the title box, text follows in slug catagory also. (hello world)
    # this forms part or the URl. example:www.codestart2021.heroky.com/helloworld
    # list_filter gives the user a by filter method, time, date or day


@admin.register(Comment)
class CommemntAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    # look at different method types.
    # These methods above give the admin user better ways to search,
    # add content or filter data by date, time or day. useful
    # to add to project!!

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        # queryset update.
        # updated to approved is True
        # Commemts can now be approved by admin user
