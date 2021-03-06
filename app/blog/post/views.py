from django.shortcuts import render, get_object_or_404
from post.models import News, Comments
from post.forms import CommentForm
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .models import Post
from .forms import PostForm



def news_list(request):
    """ выводит все новости
    """
    news = News.objects.all()
    return render(request, "post/news_list.html", {"news": news})


def new_single(request, pk):
    """ Вывод статьи """
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)
    # form = CommentForm()
    return render(request,
                "post/new_single.html",
                {"new": new,
                "comments": comment
                })



class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
