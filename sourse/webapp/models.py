from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name="Автор", default="Unknown")
    content = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.pk}){self.author}: {self.title}"

    class Meta:
        db_table = "Articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
