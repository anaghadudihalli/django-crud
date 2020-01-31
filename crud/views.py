from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Users, Publications

def read(request):
    publications_list = Publications.objects.all()
    student_id_list = []
    for user in Users.objects.all():
        student_id_list.append(user.id)
    context = {'publications_list': publications_list, 'student_id_list':student_id_list}
    return render(request, 'crud/index.html', context)

def create(request):
    student_id_list = []
    for user in Users.objects.all():
        student_id_list.append([user.id, user.first_name + ' ' + user.last_name])
    context = {'student_id_list':student_id_list}
    return render(request, 'crud/create.html', context)

def update(request, publications_id):
    publication = get_object_or_404(Publications, pk=publications_id)
    return render(request, 'crud/update.html', {'publication': publication})

def delete(request, publications_id):
    publication = get_object_or_404(Publications, pk=publications_id)
    student_id = publication.student_id
    publication = student_id.publications_set.get(pk=publications_id)
    publication.delete()
    return HttpResponseRedirect(reverse('crud:read'))

def add(request):
    user = get_object_or_404(Users, pk=request.POST['student_id'])
    user.publications_set.create(title=request.POST['title'], year=request.POST['year'])
    user.save()
    return HttpResponseRedirect(reverse('crud:read'))
def add_students(request):
    return render(request, 'crud/add_students.html')

def add_s(request):
    u = Users(email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    u.save()
    return HttpResponseRedirect(reverse('crud:read'))

def edit(request, publications_id):
    publication = get_object_or_404(Publications, pk=publications_id)
    student_id = publication.student_id
    publication = student_id.publications_set.get(pk=publications_id)
    print(request.POST['title'])
    print(request.POST['year'])
    if request.POST['title']:
        publication.title = request.POST['title']
        publication.save()
    if request.POST['year']:
        publication.year = request.POST['year']
        publication.save()
    if not request.POST['title'] and not request.POST['year']:
        return render(request, 'crud/update.html', {
            'publication': publication,
            'error_message': "You didn't enter anything.",
        })

    return HttpResponseRedirect(reverse('crud:read'))







