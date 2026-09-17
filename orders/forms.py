from django import forms


class CheckoutForm(forms.Form):

    name = forms.CharField(max_length=150)

    email = forms.EmailField()

    phone = forms.CharField(max_length=20)

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 4}
        )
    )