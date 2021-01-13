from django.forms import ModelForm
from djstripe.models import PaymentMethod


class SavePaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
