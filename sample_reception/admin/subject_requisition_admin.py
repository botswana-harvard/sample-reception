from django.conf import settings
from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_lab.admin import (
    RequisitionAdminMixin,
    requisition_fieldset,
    requisition_status_fieldset,
    requisition_identifier_fieldset,
    requisition_identifier_fields,
    requisition_verify_fieldset)

from ..admin_site import sample_reception_admin
from ..models import SubjectRequisition
from ..forms import SubjectRequisitionForm


@admin.register(SubjectRequisition, site=sample_reception_admin)
class SubjectRequisitionAdmin(RequisitionAdminMixin,
                              admin.ModelAdmin):

    # show_save_next = False

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'sample_reception_dashboard_url')

    form = SubjectRequisitionForm

    ordering = ('requisition_identifier', )

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'requisition_identifier',
                'requisition_datetime',
                'panel',
                'visit_code',
                'clinician_initials',
                'protocol_number',
                'specimen_type',
                'specimen_condition',
                'site_code',
            )}),
        requisition_fieldset,
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
        'clinic_verified': admin.VERTICAL,
    }

    def visit_code(self, obj=None):
        return f'{obj.visit_code}'

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + requisition_identifier_fields)

