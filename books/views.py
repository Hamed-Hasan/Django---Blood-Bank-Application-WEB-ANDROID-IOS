from django.shortcuts import render,redirect
from . models import Purcehase_model,Book_model
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from user_accounts.models import user_account
from django.shortcuts import get_object_or_404


# Create your views here.


# email send setup starts here -------------------------
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

# email send setup ends here ---------------------------------

def purchased_view(request,id):
    filtered_book_model = Book_model.objects.get(pk=id)
    purchase_instance = Purcehase_model()
   

    purchase_instance.user=request.user
    purchase_instance.Book=filtered_book_model
    purchase_instance.purchased_book_name=filtered_book_model.title
    purchase_instance.purchased_book_price=filtered_book_model.borrowing_price
    
    purchase_instance.balance_after_purchased=(request.user.account.balance) - (filtered_book_model.borrowing_price)
     
    purchase_instance.save()



    request.user.account.balance = purchase_instance.balance_after_purchased
    request.user.account.save()
    
    
    send_transaction_email(request.user, purchase_instance.purchased_book_price, "Purchase confimation", "purchase_email.html")

    return redirect("home")

def purchase_history(request):
    purchase_all_history= Purcehase_model.objects.filter(relatin_with_user= request.user)
    return render(request,"purchase_history.html",{'data':purchase_all_history})


# def books_details(request,id):
#     filter_book = Book_model.objects.filter(id=id)
    
#     return redirect(request,"books_details.html",{'data':filter_book})


def books_details(request,id):
     data = Book_model.objects.filter(pk=id)
     return render(request,"books_details.html",{'data':data})

# class BookDetailsView(DetailView):
#     model = Book_model
#     pk_url_kwarg = 'id'
#     template_name='books_details.html'

   

    # def post(self, request, *args, **kwargs):
    #     comment_form = forms.CommentForm(data=self.request.POST)
    #     post = self.get_object()
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()
    #     return self.get(request, *args, **kwargs)
    
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = self.object
    #     comments = post.comments.all()
    #     comment_form = forms.CommentForm()
    #     context['comments']= comments
    #     context['comment_form'] = comment_form
    #     return context


def return_book(request,id):
    #  filtered_book = Book_model.objects.get(pk=id)
     
     filtered_book = get_object_or_404(Purcehase_model, pk=id)

     book_price = filtered_book.purchased_book_price

     print("printing book price",book_price)

     user_balance = request.user.account.balance

     #giving user's money back

     user_balance=user_balance+book_price
     print("printing user balance : ",user_balance)
     request.user.account.balance = user_balance
     request.user.account.save()

     filtered_book.delete()

     return redirect("home")


