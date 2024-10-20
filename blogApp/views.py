from django.shortcuts import render

posts = [
    {
        "author": "Sanjeev",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2024",
    },
    {
        "author": "Tom",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2024",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blogApp/home.html", context)


def about(request):
    return render(request, "blogApp/about.html", {"title": "About"})
