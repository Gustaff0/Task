# Generated by Django 3.1.7 on 2021-03-11 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'New'), ('in_progress', 'In_progress'), ('done', 'Done')], max_length=200)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('tusk', 'Tusk'), ('bug', 'Bug'), ('enhancement', 'Enhancement ')], max_length=200)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
                'db_table': 'Type',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('summary', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='webapp.status', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='webapp.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'Task',
            },
        ),
    ]
