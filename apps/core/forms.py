# apps/core/forms.py
from django import forms

SERVICE_CHOICES = [
    ("", "Select a service..."),
    ("web_development", "Web & System Development"),
    ("it_consultation", "IT Consultation"),
    ("digital_transformation", "Digital Transformation"),
    ("other", "Other"),
]


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Juan dela Cruz"})
    )
    work_email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "juan@company.com"})
    )
    company_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Your Company Inc."}),
    )
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+63 912 345 6789"}),
    )
    service_interest = forms.ChoiceField(choices=SERVICE_CHOICES)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Tell us about your project...", "rows": 4}
        )
    )
