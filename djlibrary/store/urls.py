from django.urls import re_path

from .views import (
    create_book_normal,
    create_book_model_form,
    create_book_with_authors,
    BookListView,
    add_records_into_two_models,

)

app_name = 'store'

urlpatterns = [

    re_path(r'^book/create_normal', create_book_normal, name='create_book_normal'),
    re_path(r'^book/create_model', create_book_model_form, name='create_book_model_form'),
    re_path(r'^book/create_with_author', create_book_with_authors, name='create_book_with_authors'),
    re_path(r'^book/list', BookListView.as_view(), name='book_list'),
    re_path(r'^book/add_services_workers', add_records_into_two_models, name='add_records_into_two_models'),
    

]