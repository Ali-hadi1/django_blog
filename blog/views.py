from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set =  super().get_queryset()
        data = query_set[:3]
        return data    

class AllPostsListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {'post': post, 'tags': post.tags.all(), 'comment_form': CommentForm()}
        return render(request, 'blog/post-details.html', context)

    def post(self, request, slug):
        comment_form = CommentForm()
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-details'), args=[slug])
        
        context = {'post': post, 'tags': post.tags.all(), 'comment_form': CommentForm()}
        return render(request, 'blog/post-details.html', context)


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post-details.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["tags"] = self.object.tags.all() 
#         context["comment_form"] = CommentForm
#         return context
    


def get_date(post):
    return post.get('date')

# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, 'blog/index.html', {'posts': latest_posts})

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, 'blog/posts.html', {'posts': all_posts})

# def post_details(request, slug):
#     # post = Post.objects.get(slug=slug)
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-details.html', { 'post': post,  'tags': post.tags.all()})