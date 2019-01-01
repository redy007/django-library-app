from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    BookFormset,
    BookModelFormset,
    BookModelForm,
    AuthorFormset,
    ServiceFormset,
    WorkerFormset,
    ServiceWorkerFormset
)
from .models import Book, Author, ServicesWorkers, Worker, Service


def create_book_normal(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            return redirect('store:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class BookListView(generic.ListView):

    model = Book
    context_object_name = 'books'
    template_name = 'store/list.html'


def create_book_model_form(request):
    template_name = 'store/create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('store:book_list')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


def create_book_with_authors(request):
    template_name = 'store/create_with_author.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = book
                author.save()
            return redirect('store:book_list')
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })

def add_records_into_two_models(request):
    template_name = 'store/create_services_with_workers.html'
    if request.method == 'GET':
        service_formset = ServiceFormset(queryset=Service.objects.none(), prefix='services')
        workers_formset = WorkerFormset(queryset=Worker.objects.none(), prefix='workers')
        # service_workers_formset = ServiceWorkerFormset(queryset=ServicesWorkers.objects.none(), prefix='checkbox')
    elif request.method == 'POST':
        service_formset = ServiceFormset(request.POST, prefix='services')
        workers_formset = WorkerFormset(request.POST, prefix='workers')
        if service_formset.is_valid() and workers_formset.is_valid():
            # first save this service, as its reference will be used in `ServicesWorkers record`
            list_service_id = []
            service_form_position = 0
            
            for services in service_formset:
                service = services.save()
                list_service_id.append(service)
                worker_form_position = 0

                for form in workers_formset:
                    # so that `worker` instance can be attached.
                    worker = form.save()                    

                    checkbox = "checkbox_service_" + str(service_form_position) + "_worker_" + str(worker_form_position)
                    if checkbox in request.POST:
                        #checkbox has been checked
                        serviceWorker = ServicesWorkers.objects.create(service=list_service_id[service_form_position], worker=worker, service_enabled='T')
                    else:
                        #it is not checked
                        serviceWorker = ServicesWorkers.objects.create(service=list_service_id[service_form_position], worker=worker, service_enabled='F')

                    worker_form_position += 1
                service_form_position += 1
            return redirect('store:book_list')
    return render(request, template_name, {
        'service_formset': service_formset,
        'workers_formset': workers_formset,
    })