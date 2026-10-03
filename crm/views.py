from django.shortcuts import render
from .forms import CreateForm, ManagerForm
from .models import Lead, Manager, Admin, StorageModel, PostModel
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class LeadsViews(ListView):
    model = Lead
    template_name = 'leads.html'
    context_object_name = 'leads'
    def get_queryset(self):
        return Lead.objects.all()


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'lead.html'
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    model = Lead
    form_class = CreateForm
    template_name = 'leadcreate.html'
    success_url = reverse_lazy('crm:lead_url')

class LeadUpdateView(UpdateView):
    model = Lead
    form_class = CreateForm
    template_name = 'lead_update.html'
    success_url = reverse_lazy('crm:lead_url')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'lead_confirm_delete.html'
    success_url = reverse_lazy('crm:lead_url')
    def get_object(self, queryset = ...):
        return Lead.objects.get(id = self.kwargs['id'])

class ManagersViews(ListView):
    model = Manager
    template_name = 'managers.html'
    context_object_name = 'managers'
    def get_queryset(self):
        return Manager.objects.all()


class ManagerDetailView(DetailView):
    model = Manager
    template_name = 'manager.html'
    context_object_name = 'manager'

class ManagerCreateView(CreateView):
    model = Manager
    form_class = ManagerForm
    template_name = 'managercreate.html'
    success_url = reverse_lazy('crm:manager_url')

class storageListView(ListView):
    model = StorageModel
    template_name = 'storage_list.html'
    context_object_name = 'storages'

class StorageDetailView(DetailView):
    model = StorageModel
    template_name = 'storage_detail.html'
    context_object_name = 'storage'

class PostListView(ListView):
    model = PostModel
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = PostModel
    template_name = 'post_detail.html'
    context_object_name = 'post'

