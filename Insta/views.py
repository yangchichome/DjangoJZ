from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post

class HelloWorld(TemplateView):
    template_name = 'test.html'


class PostsView(ListView):
    model = Post
    template_name = 'Index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

 