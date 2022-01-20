from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect, render

from todo.models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = Todo(text=request.POST["text"])
        form.save()
        return redirect('todo')

    page = {
        "list": item_list,
        "title": "TODO LIST"
    }

    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
