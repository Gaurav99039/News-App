from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class Article_list_view(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'

class Article_detail_view(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'

class Article_edit_view(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['author','title','body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Article_Delete_view(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class Article_create_view(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title','body']
    success_url = reverse_lazy('article_list')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
