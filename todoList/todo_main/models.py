from django.db import models

# Create your models here.
# 처음 화면 display
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=50, null=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.title