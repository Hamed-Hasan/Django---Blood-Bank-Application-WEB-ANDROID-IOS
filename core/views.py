from django.shortcuts import render
from django.core.paginator import Paginator
from catagories.models import Category_model
from books.models import Book_model

# Create your views here.
def home(request, book_model_slug=None):
    book_model_details = Book_model.objects.all()
    if book_model_slug is not None:
        book_model_slug_field = Category_model.objects.get(slug=book_model_slug)
        book_model_details = Book_model.objects.filter(categories=book_model_slug_field)

    category_details = Category_model.objects.all()

    # Pagination
    paginator = Paginator(book_model_details, 6)  # Show 6 books per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "./home.html", {'category_details': category_details, 'page_obj': page_obj})



