from django.db import models
from catagories.models import Category_model
from django.contrib.auth.models import User
from user_accounts.models import user_account


class Book_model(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='books/media/uploads/', blank=True, null=True)
    borrowing_price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category_model, related_name='category')
    user_reviews = models.ManyToManyField(User, through='books.Review')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book_model, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.book}"
    
class Purcehase_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    Book = models.ForeignKey(Book_model,on_delete=models.CASCADE)
    is_Borrowd = models.BooleanField(default=True, null = True, blank = True)

    purchased_book_name = models.TextField(blank=True,null=True)
    purchased_book_price = models.IntegerField(blank=True,null=True)
    balance_after_purchased=models.IntegerField(blank=True,null=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.user.first_name} borrowed this book name: {self.Book.title}"
