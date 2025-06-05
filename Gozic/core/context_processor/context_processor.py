from Support.models import Field

def get_field(request):
    allField = Field.objects.all().order_by('id')
    
    return {"allField":allField}