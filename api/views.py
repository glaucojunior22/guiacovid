# from django.views import View
# from django.http import JsonResponse
from rest_framework import viewsets, generics
from .serializers import SourceSerializer, CategorySerializer, TagSerializer
from portal.models import Category, Source, Tag


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SourceByCategoryList(generics.ListAPIView):
    serializer_class = SourceSerializer

    def get_queryset(self):
        category_name = self.kwargs['category']
        return Source.objects.filter(category__name=category_name)


class SourceByTagList(generics.ListAPIView):
    serializer_class = SourceSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag']
        return Source.objects.filter(tag__name=tag_name)

# class SourceList(View):
#     model = Source

#     def get(self, request):
#         records = Source.objects.all()
#         items = []
#         for record in records:
#             items.append({
#                 'title': record.title,
#                 'description': record.description,
#                 'url': record.url,
#                 'category': record.category.name,
#                 'tags': [
#                     tag.name for tag in record.tags.all()
#                 ]
#             })
#         return JsonResponse(items, safe=False)


# class TagList(View):
#     model = Tag

#     def get(self, request):
#         records = Tag.objects.all()
#         items = []
#         for record in records:
#             items.append({
#                 'name': record.name
#             })
#         return JsonResponse(items, safe=False)


# class CategoryList(View):
#     model = Category

#     def get(self, request):
#         records = Category.objects.all()
#         items = []
#         for record in records:
#             items.append({
#                 'name': record.name
#             })
#         return JsonResponse(items, safe=False)