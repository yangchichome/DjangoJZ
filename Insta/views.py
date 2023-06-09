from annoying.decorators import ajax_request
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from Insta.models import Post, Like, InstaUser, UserConnection
from Insta.forms import CustomUserCreationForm
from django.db.models import Q

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'Index.html'
    login_url = "login"

    def get_queryset(self):
        current_user = self.request.user
        following = set([current_user])
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(Q(author__in=following) | Q(author=current_user))

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
