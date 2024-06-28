from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import Education


def index(request):
    education = Education.objects.order_by("end_date")
    template = loader.get_template("ml_pf/index.html")
    context = dict(education=education)
    return HttpResponse(template.render(context, request))