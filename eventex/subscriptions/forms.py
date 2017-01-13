from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription


class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if (self.cleaned_data.get('email') == '' and self.cleaned_data.get('phone') == ''):
            raise ValidationError('Informe seu email ou telefone.')

        return self.cleaned_data

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        ''' linha usada para que use o clean da classe model forms, sem essa chamada o metodo clean é sobrescrito
        sem a validação de unicidade, por exemplo.'''
        self.cleaned_data = super().clean()

        if (self.cleaned_data.get('email') == '' and self.cleaned_data.get('phone') == ''):
            raise ValidationError('Informe seu email ou telefone.')

        return self.cleaned_data