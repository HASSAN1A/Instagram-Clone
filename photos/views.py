from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Username



# Create your views here.



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'photo/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'photo/home.html'
    context_object_name = 'posts'
    ordering  = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'photo/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image',]
    template_name="photo/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name="photo/post_form.html"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Post
    success_url = '/'
    template_name="photo/post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def register(request):
    return render(request, 'users/register.html')


def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_username = Username.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"username": searched_username})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})

