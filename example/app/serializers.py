from .models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=True)

    def create(self, validated_data):
        author, _ = Author.objects.get_or_create(**validated_data['author'])
        return Book.objects.create(author=author, name=validated_data['name'])

    class Meta:
        model = Book
        fields = '__all__'
