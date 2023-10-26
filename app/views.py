from django.shortcuts import render
from .models import ChronologicalRecord
from django.views.generic.edit import CreateView
from .forms import ChronologicalRecordForm
# Create your views here.

def single_record(request, record_id):
    record = ChronologicalRecord.objects.get(pk=record_id)
    return render(request, 'single_record.html', {'record': record})

def all_records(request):
    records = ChronologicalRecord.objects.all().order_by('-created_at')
    return render(request, 'all_records.html', {'records': records})

class CreateRecordView(CreateView):
    model = ChronologicalRecord
    form_class = ChronologicalRecordForm
    template_name = 'create_record.html'
    success_url = '/all_records'