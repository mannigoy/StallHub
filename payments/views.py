from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import PaymentForm, PaymentMethodForm
from .models import Payment, PaymentMethod


def index(request):
    payments = Payment.objects.select_related('agreement', 'payment_method').order_by('payment_date', 'payment_id')
    methods = PaymentMethod.objects.order_by('method_name')
    return render(request, 'payments/index.html', {'payments': payments, 'methods': methods})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment recorded successfully.')
            return redirect('payments:index')
    else:
        form = PaymentForm()

    return render(request, 'payments/add_payment.html', {'form': form})


def add_payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment method added successfully.')
            return redirect('payments:index')
    else:
        form = PaymentMethodForm()

    return render(request, 'payments/add_payment_method.html', {'form': form})

def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect("payments:index")
    else:
        form = PaymentForm(instance=payment)

    return render(request, "payments/edit_payment.html", {"form": form})

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == "POST":
        payment.delete()
        return redirect("payments:index")

    return redirect("payments:index")  
