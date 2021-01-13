from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from djstripe.models import PaymentMethod

from django.views.generic import CreateView

from payments.forms import SavePaymentMethodForm


class UserSavePaymentMethod(LoginRequiredMixin, CreateView):
    model = PaymentMethod
    form_class = SavePaymentMethodForm
    queryset = PaymentMethod.objects.all()
    template_name = 'payments/save_payment_method.html'
