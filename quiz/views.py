from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from quiz import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='hello'
        return context


class ChapterListView(ListView):
    model=models.McqExam


class QuestionDetailView(DetailView):
    context_object_name='question'
    model=models.McqExam
    template_name='quiz/quiz_detail.html'

class ChapterCreateView(CreateView):
    fields=('exam_topic',)
    model=models.McqExam

class QuestionUpdateView(UpdateView):
    fields=('id','question','option_1','option_2','option_3','option_4','correct_ans')
    model=models.Question

class ChapterDeleteView(DeleteView):
    model=models.McqExam
    success_url=reverse_lazy('quiz:list')
