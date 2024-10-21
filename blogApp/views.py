from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.
# This function based view is not being called anymore
# The class based view below is being called instead
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blogApp/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blogApp/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]


def about(request):
    return render(request, "blogApp/about.html", {"title": "About"})
