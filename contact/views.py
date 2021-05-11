from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Contact
from .forms import CreateContactForm
from django.contrib import messages


class CreateContact(CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    form_class = CreateContactForm
    success_url = reverse_lazy('contact:create_contact')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.is_read = False
        form.save()
        messages.success(self.request, 'پیام تو با موفقیت ارسال شد.', 'success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'یه مشکلی هست ، ببین ارور چی میگه !', 'danger')
        return super().form_invalid(form)
