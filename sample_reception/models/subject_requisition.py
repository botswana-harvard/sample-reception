from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.constants import NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_lab.models import RequisitionIdentifierMixin
from edc_lab.models import RequisitionModelMixin, RequisitionStatusMixin
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base
from edc_base.sites import CurrentSiteManager, SiteModelMixin

from ..choices import REASON_NOT_DRAWN
from django.utils import timezone


class SearchSlugModelMixin(Base):

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('subject_identifier')
        return fields

    class Meta:
        abstract = True


class Manager(SearchSlugManager):
    pass


class ReceiveModelMixin(models.Model):

    specimen_condition = models.CharField(
        max_length=2,
        null=True,
        blank=True,)

    site_code = models.CharField(
        max_length=2,
        null=True,
        blank=True,)

    receive_datetime = models.DateTimeField(
        default=timezone.now)

    class Meta:
        abstract = True


class SubjectRequisition(
        NonUniqueSubjectIdentifierFieldMixin,
        RequisitionModelMixin, ReceiveModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        SearchSlugModelMixin, BaseUuidModel):

    lab_profile_name = 'sample_reception'

    reason_not_drawn = models.CharField(
        verbose_name='If not drawn, please explain',
        max_length=25,
        default=NOT_APPLICABLE,
        choices=REASON_NOT_DRAWN)

    visit_code = models.CharField(
        verbose_name='Visit Code',
        max_length=10,
        null=True)

    on_site = CurrentSiteManager()

    objects = Manager()

    history = HistoricalRecords()

    def __str__(self):
        return (
            f'{self.requisition_identifier} '
            f'{self.panel_object.verbose_name}')

    def save(self, *args, **kwargs):
        self.clinic_verified = 'Yes'
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend([
            'requisition_identifier',
            'human_readable_identifier', 'identifier_prefix'])
        return fields

    class Meta:
        unique_together = ('panel', 'subject_identifier')
