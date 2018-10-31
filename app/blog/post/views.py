from django.shortcuts import render
from post.models import News



def news_list(request):
    """ выводит все новости
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})
