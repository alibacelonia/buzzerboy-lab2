from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects, 'segment': 'project'})
        
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {'project': project, 'segment': 'project', 'tasks': tasks})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'projects/project_form.html', {'form': form, 'segment': 'project'})
    else:
        form = ProjectForm()
        print("Rendering empty form.")  # Debug line
        return render(request, 'projects/project_form.html', {'form': form, 'segment': 'project'})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=pk)
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'projects/project_form.html', {'form': form, 'segment': 'project'})
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'segment': 'project'})

@login_required
def task_detail(request, project_pk, task_pk):
    try:
        project = get_object_or_404(Project, pk=project_pk)
        task = get_object_or_404(Task, pk=task_pk, project=project)
        return render(request, 'projects/task_detail.html', {'project': project, 'segment': 'project', 'task': task})
    except:
        return redirect('project_list')

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project, 'segment': 'project'})

@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project_pk)
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'projects/task_form.html', {'form': form, 'project': project, 'segment': 'project'})
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project, 'segment': 'project'})

@login_required
def task_update(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project_pk)
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'projects/task_form.html', {'form': form, 'project': project, 'segment': 'project'})
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'project': project, 'segment': 'project'})

@login_required
def task_delete(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project_pk)
    return render(request, 'projects/task_confirm_delete.html', {'task': task, 'project': project, 'segment': 'project'})
