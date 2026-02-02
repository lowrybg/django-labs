from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Task

def index(request: HttpRequest,) -> HttpResponse:


   context = {
       'tasks' : Task.objects.all(),
   }
   return render(request, 'index.html', context)

def id_view(request: HttpRequest, num) -> HttpResponse:
    return HttpResponse(f"The type is str num {num} {type(num)}", content_type="text/plain")

def uuid_view(request: HttpRequest, uuid:str) -> HttpResponse:
    return HttpResponse(f"The type is uuid {uuid} {type(uuid)}", content_type="text/plain")


# def index2(request: HttpRequest) -> HttpResponse:
#     all_tasks = Task.objects.all()
#
#     template = [
#         '<h1>Tasks</h1>',
#         *[f"<li>{t.title} - {t.is_done}</li>" for t in all_tasks]
#     ]
#
#     return HttpResponse('\n'.join(template),
#                         content_type="text/html",
#                         )
