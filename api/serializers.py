from rest_framework import serializers
from portal.models import Source, Category, Tag

class SourceSerializer(serializers.ModelSerializer):
    # tags = serializers.StringRelatedField(many=True)
    # category = serializers.StringRelatedField()
    
    class Meta:
        model = Source
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'url', 'image', 'category',
                  'tags', 'facebook', 'instagram', 'twitter', 'whatsapp',
                  'play_store', 'app_store']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'sources']


class TagSerializer(serializers.ModelSerializer):
    # sources = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'sources']
