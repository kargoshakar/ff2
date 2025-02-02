# Generated by Django 5.1.1 on 2024-10-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0010_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, null=True, related_name='task_labels', to='labels.label', verbose_name='Labels'),
        ),
    ]
