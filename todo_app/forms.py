from django import forms
from todo_app.models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['taskTitle', 'taskDescription','id']
