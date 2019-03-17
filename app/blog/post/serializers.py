from . import models

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = (
            'pk',
            'title',
            'created',
            'body',
        )
