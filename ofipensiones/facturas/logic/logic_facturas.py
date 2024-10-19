from ..models import Factura

def get_factura(var_pk):
    factura=Factura.objects.get(pk=var_pk)
    return factura

def get_recibo(var_pk):
    recibo = Recibo.objects.get(pk=var_pk)
    facturas = recibo.factura_set.all()  
    return recibo, facturas

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
"""from models import Factura
from xhtml2pdf import pisa

def factura_pdf(request, factura_id):
    # Obtén la factura por ID
    factura = get_object_or_404(Factura, id=factura_id)

    # Renderiza la plantilla de PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.id}.pdf"'

    # Utiliza el método render_to_pdf para convertir el HTML a PDF
    template_path = 'factura_pdf.html'
    context = {'factura': factura}
    response = render_to_pdf(template_path, context, response)
    
    return response

def render_to_pdf(template_src, context_dict, response):
    template = render_to_string(template_src, context_dict)
    pdf = pisa.pisaDocument(BytesIO(template.encode("UTF-8")), response)
    return pdf
"""