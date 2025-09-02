from django import forms
from django.contrib.auth.models import User
from .models import Morador

class MoradorForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    email = forms.EmailField(label="Email")

    class Meta:
        model = Morador
        fields = ['apartamento']  # só o que tá no Morador

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        morador = super().save(commit=False)
        morador.user = user
        if commit:
            morador.save()
        return morador
