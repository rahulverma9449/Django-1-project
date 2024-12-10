from django import forms 
from .models import ChaiVarieties


class ChaiVarietiesForm(forms.ModelForm):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarieties.objects.all(), label="Select chai variety")
    class Meta:
        model = ChaiVarieties
        fields = ['chai_varity']