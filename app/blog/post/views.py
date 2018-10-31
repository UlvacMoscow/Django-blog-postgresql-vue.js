from django.shortcuts import render, get_object_or_404
from post.models import News



def news_list(request):
    """ выводит все новости
    """
    news = News.objects.all()
    return render(request, "post/news_list.html", {"news": news})


def new_single(request, pk):
    """ Вывод статьи """
    new = get_object_or_404(News, id=pk)
    return render(request, "post/new_single.html", {"new": new})
