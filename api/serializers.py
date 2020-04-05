from rest_framework import serializers
from portal.models import Source, Category, Tag

class SourceSerializer(serializers.ModelSerializer):
    # tags = serializers.StringRelatedField(many=True)
    # category = serializers.StringRelatedField()
    urls = serializers.SerializerMethodField()
    
    class Meta:
        model = Source
        # fields = '__all__'
        # fields = ['id', 'title', 'description', 'url', 'image', 'category',
        #           'tags', 'facebook', 'instagram', 'twitter', 'whatsapp',
        #           'play_store', 'app_store']
        fields = ['id', 'title', 'description', 'image', 'category', 'tags',
                  'urls']


    def get_urls(self, obj):
        print(type(obj))
        urls = []
        links = ['site', 'instagram', 'facebook', 'twitter', 'whatsapp',
                 'play_store', 'app_store']
        for link in links:
            if getattr(obj, link) is not None:
                # urls[link] = getattr(obj, link, '')
                urls.append({'app': link, 'url': getattr(obj, link, '')})
        return urls

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'sources']


class TagSerializer(serializers.ModelSerializer):
    # sources = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'sources']
