from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'portal'

router = routers.DefaultRouter()
router.register(r'sources', views.SourceViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('sources/category/<str:category>/', 
         views.SourceByCategoryList.as_view()),
    path('sources/tag/<str:tag>/', views.SourceByTagList.as_view()),
    # path('sources', views.SourceList.as_view()),
    # path('tags', views.TagList.as_view()),
    # path('categories', views.CategoryList.as_view()),
]