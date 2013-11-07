from django.http import HttpResponse
from django.template import RequestContext, loader

from flyer.models import Sale

def index(request):
    # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question for p in latest_poll_list])
    # return HttpResponse(output)

    all_sales = Sale.objects.order_by('-price_sale')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'all_sales': all_sales,
    })
    return HttpResponse(template.render(context))