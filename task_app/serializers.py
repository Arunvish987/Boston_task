from rest_framework import serializers
from .models import BookModel

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'title', 'author', 'publication_date']