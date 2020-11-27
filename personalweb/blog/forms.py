from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(label='autor',
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Tú nombre"
        })
    )
    body = forms.CharField(label='cuerpo', widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Deja un comentario"
        })
    )