from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import sample_reception_admin

app_name = 'sample_reception'

urlpatterns = [
    path('admin/', sample_reception_admin.urls),
    path('', RedirectView.as_view(url='/'), name='home_url'),
]
