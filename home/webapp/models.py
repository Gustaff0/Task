from django.db import models

# Create your models here.
class TimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Type(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = 'Type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return f"{self.name}"

class Status(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f"{self.name}"


class Task(TimeBase):
    summary = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.CASCADE, related_name='status', verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', on_delete=models.CASCADE, related_name='types', verbose_name='Тип')

    class Meta:
        db_table = 'Task'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.summary}: {self.description}'


