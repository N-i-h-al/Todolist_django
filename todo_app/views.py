from django.shortcuts import render,redirect
from todo_app.models import TodoModel
from todo_app.forms import TodoForm

def home(request):
    return render(request, 'home.html')

def add_task(request):
    if request.method == 'POST':
        task = TodoForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show_tasks')
         
    else:
        task = TodoForm()
    return render(request, 'add_task.html', {'form': task})


def show_tasks(request):
    tasks = TodoModel.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'tasks': tasks})

def delete_task(request, id):
    task = TodoModel.objects.get(pk = id).delete()
    return redirect('show_tasks')


def edit_task(request,id):
    task = TodoModel.objects.get(pk = id)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        task = TodoForm(request.POST,instance=task)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')
    return render(request, 'add_task.html', {'form': form})
    

def complete_task(request, id):
    task = TodoModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')

def completed_tasks_list(request):
    completed_tasks = TodoModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks_list.html', {'tasks': completed_tasks})




