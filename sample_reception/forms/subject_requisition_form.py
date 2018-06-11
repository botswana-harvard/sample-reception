from django import forms
from edc_lab.forms import RequisitionFormMixin
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


from ..models import SubjectRequisition

class SubjectModelFormMixin(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    pass


class SubjectRequisitionForm(SubjectModelFormMixin, RequisitionFormMixin):
    
    clinician_initials = forms.CharField(
        label='Clinician Initials')

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
