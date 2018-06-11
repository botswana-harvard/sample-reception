from edc_constants.constants import NOT_APPLICABLE, OTHER
NOT_REQUIRED = 'not_required'

REASON_NOT_DRAWN = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('collection_failed', 'Tried, but unable to obtain sample from patient'),
    ('absent', 'Patient did not attend visit'),
    ('refused', 'Patient refused'),
    ('no_supplies', 'No supplies'),
    (NOT_REQUIRED, 'No longer required for this visit'),
    (OTHER, 'Other'),)