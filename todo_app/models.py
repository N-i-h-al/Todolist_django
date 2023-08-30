from django.db import models

# Create your models here.
class TodoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.taskTitle
