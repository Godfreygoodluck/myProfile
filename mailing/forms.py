from django import forms

class ClientsMessageForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    
    from_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        })
    )

    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
            "class": "form-control",
            "placeholder": "(Optional) Mail Subject"
            }
        )
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!"
            }
        )
    ) 