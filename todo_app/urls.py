from django.urls import path
from todo_app.views import home, add_task, show_tasks,edit_task,delete_task,complete_task,completed_tasks_list
urlpatterns = [
    path('', home, name='home'),
    path('add_new_task/', add_task, name='add_task'),
    path('show_tasks/',show_tasks, name='show_tasks'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('complete_task/<int:id>/', complete_task, name='complete_task'),
    path('completed_tasks_list/', completed_tasks_list, name='completed_tasks_list'),
]

    # path('completed_task/', completed_tasks, name='completed_tasks'),
    

    # path('show/', views.show_tasks, name='show_tasks'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    # path('completed/', views.completed_tasks, name='completed_tasks'),

# from django.urls import path
# from book_app.views import home, store_book,show_books, edit_book,delete_book
# urlpatterns = [
#     path('',home),
#     path('store_new_book/',store_book,name='storebook'),