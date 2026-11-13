from django.shortcuts import redirect, render

from app.models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    return render(request, 'app/home.html',{'tasks': tasks, 'completed_tasks': completed_tasks})
def addTask(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        task1=Task(tasks=task)
        task1.save()
        return redirect('/')
    return render(request, 'app/home.html')
def complete(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('/')
def incomplete(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = False
    task.save()
    return redirect('/')
def updateData(request, id):
    d= Task.objects.get(id=id)
    if request.method == 'POST':
        task = request.POST.get('task')
        x=Task.objects.get(id=id)
        x.tasks=task
        x.save()
        return redirect('/')
    return render(request, 'app/edit.html', {'d': d})
def deleteData(request, id):
    d= Task.objects.get(id=id)
    d.delete()
    return redirect('/')