from django.urls import path
from .views import single_record, all_records, CreateRecordView

urlpatterns = [
    path('record/<int:record_id>/', single_record, name='single_record'),
    path('all_records/', all_records, name='all_records'),
    path('', CreateRecordView.as_view(), name='create_record'),
]