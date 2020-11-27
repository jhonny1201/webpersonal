from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    email = forms.CharField(max_length=254, required=True, label='Correo electrónico', widget=forms.EmailInput())
    subject = forms.CharField(max_length=100, required=False, label='Asunto')
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Deja tú mensaje aquí :)'}
        ),
        max_length=4000, required=True, label='Mensaje',
        help_text='No más de 4000 caracteres.'
    )
