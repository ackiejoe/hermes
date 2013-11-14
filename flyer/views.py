from django.http import HttpResponse
from django.template import RequestContext, loader

from flyer.models import Sale
from flyer.models import Saving

def index(request):

    all_sales = Sale.objects.order_by('-price_sale')
    template = loader.get_template('flyer/index.html')

    context = RequestContext(request, {
        'all_sales': all_sales,
    })

    return HttpResponse(template.render(context))