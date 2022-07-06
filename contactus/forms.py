from django import forms

from .models import ContactUs

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('name', 'email_contact','phone_number','subject',
                  'message_contact')