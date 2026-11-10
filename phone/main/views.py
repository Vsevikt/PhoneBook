from django.shortcuts import redirect, render
from django import forms
from django.core.validators import RegexValidator

from main.models import Person

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=30,
        validators=[RegexValidator(
            regex=r'^\+?[0-9 ]*[0-9]$',
            message='Enter a phone number using digits, spaces, and an optional + at the beginning.',
        )],
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone number',
            'inputmode': 'tel',
            'pattern': r'\+?[0-9 ]*[0-9]',
            'title': 'Use digits, spaces, and an optional + at the beginning.',
            'data-phone-validation': 'true',
        }),
    )

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'notes')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes (optional)'}),
        }

def home(request):
    contacts = Person.objects.order_by('last_name', 'first_name')
    return render(request, 'main/index.html', {'contacts': contacts})

def contact_form(request, title, button, person=None):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if person:
                for field, value in form.cleaned_data.items():
                    setattr(person, field, value)
                person.save()
            else:
                form.save()
            return redirect('home')
    else:
        initial = {}
        if person:
            for field in ContactForm.Meta.fields:
                initial[field] = getattr(person, field)
        form = ContactForm(initial=initial)

    return render(request, 'main/contact_form.html', {
        'form': form,
        'title': title,
        'button': button,
    })

def create_contact(request):
    return contact_form(request, 'Add contact', 'Add contact')

def delete_contact(request):
    if request.method == 'POST':
        Person.objects.filter(id=request.POST.get('person')).delete()
    return redirect('home')

def update_contact(request, pk):
    person = Person.objects.filter(id=pk).first()
    if not person:
        return redirect('home')
    return contact_form(request, 'Edit contact', 'Save changes', person)
