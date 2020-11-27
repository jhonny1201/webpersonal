from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=20, required=True)
    last_name = forms.CharField(label='Apellido', required=True, max_length=209)
    email = forms.CharField(label='Correo electrónico', required=True, widget=forms.EmailInput())
    subject = forms.CharField(label='Asunto', required=False, max_length=30)
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea())