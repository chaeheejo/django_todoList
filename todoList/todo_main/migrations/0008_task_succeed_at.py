# Generated by Django 3.0 on 2022-02-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0007_task_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='succeed_at',
            field=models.DateField(null=True),
        ),
    ]