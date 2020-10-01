# Task2
It is a to-do application which provides a list of task to be done with functionalities of an update, delete and add a new task to the list.
It uses Django, HTML and CSS.

![SS1](https://user-images.githubusercontent.com/61556757/94679489-d072b980-033d-11eb-8411-633528473463.JPG)

## Creation of List
For creating this application the first step was to create a Django app.
In that, created a home-page`(list)` so that this will work as a home-page of the application and make the URL for that home page.

```from django.urls import path
from . import views
app_name = 'tasks'
urlpatterns=[
    path('',views.index, name='list'),
```
in this url there is a parameter called `views.index` which is a function written in views.py ,this basically tells the what to do when this URL is called or clicked.
```
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks:list')     # or use redirect('/') to remain in same homepage
    context = {'tasks':tasks, 'form':form} #values to be display to the user with the help of template
    return render(request,'tasks/list.html', context)
 ``` 
In this function `tasks` variable stores the data which is retrieved through the database. This database is created with the help of the `models.py` file which consists of the user-defined model.
```
from django.db import models
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=180)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
 ```
 Now next parameter in the `views.py` file for the home-page is the `form` which, basically used to display the fields to the user, this fields are the input for the user task list,with the help of `forms.py`, we can retrieve each field use it in our `views.py` and then render into the user with the help of the template through the render function.
```
from django import forms
from django.forms import ModelForm
from .models import Task
class  TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = '__all__'
 ```
After that in our views for the home-page, there is a condition which checks the whether the request which is made by a user is a POST request or not, if it is a POST request then it takes the request as a parameter into our ` form = TaskForm(request.POST)` so that whatever the user has given the input(which was shown to the user with the help of form) this data is then validated if it valid ` if form.is_valid():` then it is saved in the database ` form.save()` and the user is redirected to that same page only 
 `return redirect('tasks:list')     # or use redirect('/') to remain in same homepage`.

 ## Update and Delete

So when the user is on the home-page they get to see two buttons update and delete. When the user clicks the update button then a new page pops-up, in that page it provides two options if the tasks are complete then click the complete box or else update the task and then submit it and the user task list gets updated.
Again for this process, all the validation is done by the update view in `views.py`.

![SS2](https://user-images.githubusercontent.com/61556757/94691232-af669480-034e-11eb-9857-f01432a7bf7c.JPG)

For the delete operation when the user clicks on that option they will see a confirmation whether they have to delete it or they can cancel this operation. If they cancel the operation then they are redirected to the home-page and nothing is done, else when clicked delete, then with the help of the  `id` of that task it has been deleted from the database.

![SS3](https://user-images.githubusercontent.com/61556757/94700021-a2e73980-0358-11eb-85cd-9f3aa8f4fc4c.JPG)
