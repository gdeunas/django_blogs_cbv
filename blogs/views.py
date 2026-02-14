from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blogs.models import Record
from django import forms


class RecordListView(ListView):
    model = Record
    template_name = 'blogs/records_list.html'
    context_object_name = 'records'


class RecordDetailView(DetailView):
    model = Record
    template_name = 'blogs/record_detail.html'
    context_object_name = 'record'


class RecordCreateView(CreateView):
    model = Record
    fields = ['title', 'content', 'is_published']
    template_name = 'blogs/record_form.html'
    success_url = reverse_lazy('blogs:records_list')


class RecordUpdateView(UpdateView):
    model = Record
    fields = ['title', 'content']
    template_name = 'blogs/record_form.html'
    success_url = reverse_lazy('blogs:records_list')


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'blogs/record_delete.html'
    success_url = reverse_lazy('blogs:records_list')


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'content', 'image', 'number_of_views']
