from django.shortcuts import render, render_to_response, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
import datetime
from .models import Quest, Choice
from .forms import QuestForm, LogForm

def index(request):
    return HttpResponse("Halo")

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        """Return the last five published quests."""
        return Quest.objects.order_by('-pub_date')[:25]


class DetailView(generic.DetailView):
    model = Quest
    template_name = 'todo/detail.html'

    def index(request):
        return redirect('todo:index')

def new_quest(request):
    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('todo:index')
    else:
        form = QuestForm()

    return render(request, 'todo/quest_form.html', {'form': form})

def new_log(request, quest_id):
    quest1 = get_object_or_404(Quest, pk=quest_id)


    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('todo:index')

    else:
        form = LogForm(initial={'choice_text': 'example text', 'quest': quest1})

    return render(request, 'todo/choice_form.html', {'form': form})


class QuestDelete(DeleteView):
    model = Quest
    success_url = reverse_lazy('todo:index')
