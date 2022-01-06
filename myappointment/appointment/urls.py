from django.urls import path,include,re_path
from appointment.views import (
    AppointmentCreateView,
    AppointmentDeleteView,
    AppointmentDetailView,
    AppointmentListView,
    AppointmentUpdateView,
)
app_name = 'appointment'
urlpatterns = [
    re_path(r'^new$', AppointmentCreateView.as_view(), name='new_appointment'),
   
]