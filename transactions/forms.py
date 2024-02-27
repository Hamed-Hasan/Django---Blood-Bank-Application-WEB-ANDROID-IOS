from django import forms
from . models import transaction_model

class transaction_form(forms.ModelForm):
    class Meta:
        model= transaction_model
        fields = ['amount']

    def __init__(self,*args,account=None,**kwargs):
        super().__init__(*args, **kwargs)
        self.account= account

    def save(self,commit=True):
        self.instance.account = self.account
        return super().save(commit)

class Deposite_form(transaction_form):
    def clean_amount(self):
        min_deposite_amount=100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposite_amount:
            raise forms.ValidationError(
                f'you need to deposite more than 100'
            )
        return amount


