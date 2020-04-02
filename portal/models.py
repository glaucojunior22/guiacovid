from django.db import models


class Category(models.Model):
    name = models.CharField('nome', max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Source(models.Model):
    title = models.CharField('titulo', max_length=100)
    description = models.TextField('descrição', max_length=500)
    category = models.ForeignKey(Category, models.CASCADE, 'sources', 'source')
    url = models.CharField('URL', max_length=255)
    image = models.ImageField('imagem', upload_to='uploads', null=True)

    class Meta:
        verbose_name = 'Fonte de dados'
        verbose_name_plural = 'Fontes de dados'

    def __str__(self):
        return self.title

    def get_tags(self):
        return [x for x in self.tags]


class Tag(models.Model):
    name = models.CharField('nome', max_length=100)
    sources = models.ManyToManyField(Source, 'tags', 'tag')

    def __str__(self):
        return self.name