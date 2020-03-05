from django import forms

class CreateTicketForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    description = forms.Textarea(attrs=None)
    department = forms.CharField(max_length=20)
    CHOICES = ['Urgent','High','Medium','Low']
    priority = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    seat  = forms.CharField(max_length=4)
    status = forms.IntegerField(widget=forms.HiddenInput())
    userName = forms.CharField(widget=forms.HiddenInput(),max_length=100,initial='{{request.user.username}}')