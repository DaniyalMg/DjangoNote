from django.shortcuts import render

from .form import NoteForm
from .models import Note


def getnote(request):
    if request.method == 'GET':

        form = NoteForm()

        return render(request, 'test/addnote.html', context={'form': form})
    elif request.method == 'POST':

        form = NoteForm(request.POST)
        form.instance.author = request.user

        if form.is_valid():
            form.save()

        form = NoteForm()

        return render(request, 'test/addnote.html', context={'form': form})


def note(request):
    if request.method == 'GET':

        notes = Note.objects.filter(author=request.user)

        return render(request, 'test/note.html', context={'notes': notes})
