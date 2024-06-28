from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import Education, Image
from django.utils.html import mark_safe


def index(request):
    education = Education.objects.order_by("end_date")
    image = Image.objects.get(image_type="profile_picture")
    image.image_desc = image.image_desc.replace("\\n", "<br/>")
    template = loader.get_template("ml_pf/index.html")
    context = dict(education=education, image=image)
    return HttpResponse(template.render(context, request))