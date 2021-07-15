from django import forms
from club.models import Member
class MemberForm(forms.ModelForm):

    # profile = forms.CharField(required=False)
    # introduction = forms.CharField(required=False)
    profile = forms.ImageField(required=False)

    # create meta class
    class Meta:
        # specify model to be used
        model = Member
 
        # specify fields to be used
        fields = ('generation', 'birth_date', 'email', 'profile', 'phone_number', 'introduction')
        widgets = {
        'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }