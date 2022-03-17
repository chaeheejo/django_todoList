from django.db import models

# Create your models here.
class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=50, null=True)
    due_date = models.DateField(null=True)
