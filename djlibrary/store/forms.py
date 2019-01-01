from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import (Book, Author, Service, Worker, ServicesWorkers)


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )

BookFormset = formset_factory(BookForm)

class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', )
        labels = {
            'name': 'Book Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
                }
            )
        }

BookModelFormset = modelformset_factory(
    Book,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
            }
        )
    }
)

AuthorFormset = modelformset_factory(
    Author,
    fields=('name', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Author Name here'
        })
    }
)

ServiceFormset = modelformset_factory(
    Service,
    fields=('service_name', ),
    extra=1,
    widgets={'service_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter the service's name",
        })
    }
)

WorkerFormset = modelformset_factory(
    Worker,
    fields=('worker_name', ),
    extra=1,
    widgets={'worker_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter the worker's name",
        })
    }
)

ServiceWorkerFormset = modelformset_factory(
    ServicesWorkers,
    fields=('service_enabled', ),
    extra=0,
    widgets={'service_enabled': forms.CheckboxInput(attrs={
            'class': 'form-control',
        })
    }
)