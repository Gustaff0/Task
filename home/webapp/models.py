from django.db import models
from webapp.validator import MinLengthValidator

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
    summary = models.CharField(max_length=300, null=False, blank=False, validators=(MinLengthValidator(5),))
    description = models.TextField(max_length=3000, null=True, blank=True, validators=(MinLengthValidator(5),))
    status = models.ForeignKey('webapp.Status', on_delete=models.CASCADE, related_name='status', verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='tasks', through='webapp.TaskType', through_fields=('task', 'type'))
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='project', verbose_name='Статус')

    class Meta:
        db_table = 'Task'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.summary}: {self.description}'



class TaskType(models.Model):
    task = models.ForeignKey('webapp.Task', related_name='task_type', on_delete=models.CASCADE, verbose_name='Задача')
    type = models.ForeignKey('webapp.Type', related_name='type_task', on_delete=models.CASCADE, verbose_name='Тег')

    def __str__(self):
        return "{} | {}".format(self.task, self.type)

class Project(models.Model):
    timestart = models.DateField(null=False, blank=False)
    timefinish = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=300, null=False, blank=False, validators=(MinLengthValidator(4),))
    description = models.TextField(max_length=3000, null=False, blank=False, validators=(MinLengthValidator(10),))

    class Meta:
        db_table = 'Project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name} : {self.description}'




