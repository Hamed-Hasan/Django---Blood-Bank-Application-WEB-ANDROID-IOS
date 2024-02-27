from django.shortcuts import render
from catagories.models import Category_model
from books.models import Book_model

# Create your views here.
def home(request,book_model_slug=None):

    book_model_detials = Book_model.objects.all()
    if book_model_slug is not None:
        book_mode_slug_field= Category_model.objects.get(slug=book_model_slug)
        book_model_detials= Book_model.objects.filter(categories=book_mode_slug_field)

    catagory_details = Category_model.objects.all()
    return render(request,"./home.html",{'catagory_details':catagory_details,'book_model_detials':book_model_detials})





