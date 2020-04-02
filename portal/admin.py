from django.contrib import admin
from .models import Category, Source, Tag


admin.site.register([Category, Source, Tag])