from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import transaction_form,Deposite_form
from django.views.generic import CreateView
from . models import transaction_model
from django.urls import reverse_lazy
from django.contrib import messages

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



class transactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name='transactions_form.html'
    model= transaction_model
    success_url = reverse_lazy("home")

    def get_form_kwargs(self) :
        kwargs = super().get_form_kwargs()

        kwargs.update(
            {
                'account':self.request.user.account

                },
        )
        return kwargs

class depositeMoneyView(transactionCreateMixin):
    form_class = Deposite_form

    def form_valid(self, form):
        
        # amount = form.cleaned_date.get("amount")
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account

        #creating an instance of transactions 
        transaction= form.save(commit=False)
        transaction.account = account
        transaction.save()

        #updating 

        account.balance += amount
        print("after update balance : ",amount)
        account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'{amount} was deposited form your account'
        )

        send_transaction_email(self.request.user, amount, "Deposite Message", "deposite_email.html")

        return super().form_valid(form)
    

    