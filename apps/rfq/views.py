from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from .models import RFQ
from .forms import RFQForm
from .emails import send_rfq_notifications
from apps.products.models import Product

class RFQSubmitView(View):
    template_name = 'rfq/rfq_form.html'

    def get(self, request, *args, **kwargs):
        initial_data = {}
        product_slug = request.GET.get('product')
        preselected_product = None

        if product_slug:
            try:
                preselected_product = Product.objects.get(slug=product_slug, is_active=True)
                initial_data['product'] = preselected_product
            except Product.DoesNotExist:
                pass

        form = RFQForm(initial=initial_data)
        return render(request, self.template_name, {
            'form': form,
            'preselected_product': preselected_product,
            'meta_title': 'Request for Quotation (RFQ) | STELLAR SHIPERS',
            'meta_desc': 'Submit a B2B RFQ for verified natural fibers and bio-industrial raw materials. Get certified technical specifications and competitive direct-mill pricing.'
        })

    def post(self, request, *args, **kwargs):
        form = RFQForm(request.POST, request.FILES)
        if form.is_valid():
            rfq = form.save()
            # Trigger notification emails
            send_rfq_notifications(rfq)
            # Store reference_id in session for secure display on success page
            request.session['last_rfq_ref'] = rfq.reference_id
            return redirect('rfq:success')
        
        # If invalid
        messages.error(request, 'Please correct the highlighted errors in the form before submitting.')
        source_page = request.POST.get('source_page')
        if source_page == 'contact':
            return render(request, 'pages/contact_rfq.html', {
                'form': form,
                'meta_title': 'Contact Export Desk & RFQ | STELLAR SHIPERS',
                'meta_desc': 'Directly contact our international trade team or submit a technical Request for Quotation (RFQ). Fast response within 24-48 business hours.'
            })

        return render(request, self.template_name, {
            'form': form,
            'meta_title': 'Request for Quotation (RFQ) | STELLAR SHIPERS',
            'meta_desc': 'Submit a B2B RFQ for verified natural fibers and bio-industrial raw materials.'
        })


class RFQSuccessView(TemplateView):
    template_name = 'rfq/rfq_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ref = self.request.session.get('last_rfq_ref', 'RFQ-PENDING')
        rfq_obj = None
        if ref != 'RFQ-PENDING':
            rfq_obj = RFQ.objects.filter(reference_id=ref).first()
        context['reference_id'] = ref
        context['rfq'] = rfq_obj
        context['meta_title'] = 'RFQ Submitted Successfully | STELLAR SHIPERS'
        return context
