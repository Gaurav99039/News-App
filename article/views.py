from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.

class Article_list_view(ListView):
    model = Article
    template_name = 'article_list.html'

class Article_detail_view(DetailView):
    model = Article
    template_name = 'article_detail.html'

class Article_edit_view(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['author','title','body']

class Article_Delete_view(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    