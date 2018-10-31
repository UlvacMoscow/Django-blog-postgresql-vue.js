from django.shortcuts import render, get_object_or_404
from post.models import News



def news_list(request):
    """ выводит все новости
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def news_single(request, pk):
    new = get_object_or_404(News, id=pk)
    return render(request, "news/new_single.html", {"news": new})
