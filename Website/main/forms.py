from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    message = forms.CharField(
        min_length=20,
        widget = forms.Textarea(
            attrs = {'placeholder': 'Сообщение', 'cols': 30, 'rows': 9 }
        )
    )