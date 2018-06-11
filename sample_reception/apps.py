from django.conf import settings
from django.apps import AppConfig as DjangoApponfig

class AppConfig(DjangoApponfig):
    name = 'sample_reception'
    verbose_name = 'LIS Sample Reception'


if settings.APP_NAME == 'sample_reception':

    import os

    from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
    from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
    from edc_label.apps import AppConfig as BaseEdcLabelAppConfig

    class EdcLabAppConfig(BaseEdcLabAppConfig):
        base_template_name = 'lis/base.html'
        requisition_model = 'sample_reception.subjectrequisition'
        result_model = 'edc_lab.result'

        @property
        def site_name(self):
            return 'Gaborone'

        @property
        def site_code(self):
            return '40'

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '092'


    class EdcLabelAppConfig(BaseEdcLabelAppConfig):
        template_folder = os.path.join(
            settings.STATIC_ROOT, 'lis', 'label_templates')
