from django import forms

from .models import Payment, PaymentMethod


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['method_name']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'agreement',
            'payment_method',
            'amount_paid',
            'payment_status',
            'payment_period',
            'period_month',
            'period_year',
        ]

    def clean(self):
        cleaned_data = super().clean()
        payment_period = cleaned_data.get('payment_period')
        period_month = cleaned_data.get('period_month')
        period_year = cleaned_data.get('period_year')

        if payment_period == 'monthly' and not period_month:
            self.add_error('period_month', 'Month is required for monthly payments.')
        if not period_year:
            self.add_error('period_year', 'Year is required.')

        return cleaned_data

