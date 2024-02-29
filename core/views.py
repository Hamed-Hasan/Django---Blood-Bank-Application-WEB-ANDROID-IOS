from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catagories.models import Category_model
from books.models import Book_model
from django.core.paginator import Paginator

def home(request, book_model_slug=None):
    category_details = Category_model.objects.all()
    if book_model_slug:
        # Use get_object_or_404 to avoid DoesNotExist exception
        book_model_slug_field = get_object_or_404(Category_model, slug=book_model_slug)
        book_model_details = Book_model.objects.filter(categories=book_model_slug_field)
    else:
        book_model_details = Book_model.objects.all()

    query = request.GET.get('q')
    if query:
        book_model_details = book_model_details.filter(title__icontains=query)

    # Pagination
    paginator = Paginator(book_model_details, 6)  # Show 6 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {
        'category_details': category_details,
        'page_obj': page_obj,
        'query': query
    })