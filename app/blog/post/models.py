from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    """ Класс категорий
    """
    title = models.CharField("Name category", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title



class Tag(models.Model):
    """ Класс тэгов
    """
    title = models.CharField("Name tag", max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title



class News(models.Model):
    """ Класс новостей
    """
    User = models.ForeignKey(User, verbose_name="Author")
    title = models.CharField("title", max_length=100)
    text_min = models.TextField("min chars", max_length=350)
    text = models.TextField("Text news")
    created = models.DateTimeField("Date created", auto_now_add=True)
    description = models.CharField("Info", max_length=100)
    keywords = models.CharField("keywords", max_length=50)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "All news"

    def __str__(self):
        return self.title
