from django import forms
from .models import RFQ
from apps.products.models import Product

class RFQForm(forms.ModelForm):
    # Honeypot field to trap automated spam bots
    website_check = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'hidden', 'tabindex': '-1', 'autocomplete': 'off'}),
        label=''
    )

    class Meta:
        model = RFQ
        fields = [
            'name', 'company', 'country', 'email', 'phone',
            'product', 'product_interest', 'quantity', 'application',
            'technical_requirements', 'technical_file', 'packaging',
            'delivery_country', 'incoterms', 'message',
            'sample_request', 'consent'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., Jonathan Vance, VP Procurement'
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., NovaTech Composites GmbH'
            }),
            'country': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., Germany'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'name@enterprise.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': '+49 89 12345678 (Direct / WhatsApp)'
            }),
            'product': forms.Select(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors'
            }),
            'product_interest': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'Or specify custom raw material / specification needed'
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., 20 Metric Tons / trial lot 5 MT'
            }),
            'application': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., Compression molded door panels for automotive'
            }),
            'technical_requirements': forms.Textarea(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors h-24',
                'placeholder': 'Specify target tensile strength, moisture threshold, staple length, fiber diameter, degumming protocol...'
            }),
            'technical_file': forms.FileInput(attrs={
                'class': 'w-full text-sm text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-xs file:font-semibold file:bg-slate-800 file:text-slate-200 hover:file:bg-slate-700 cursor-pointer'
            }),
            'packaging': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., 100kg hydraulic bales with PP wrap / Palletized'
            }),
            'delivery_country': forms.TextInput(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors',
                'placeholder': 'e.g., Port of Hamburg, Germany or Rotterdam, NL'
            }),
            'incoterms': forms.Select(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-slate-900/80 border border-slate-700/80 focus:border-slate-400 focus:ring-1 focus:ring-slate-400 text-white rounded px-4 py-3 text-sm placeholder-slate-500 transition-colors h-20',
                'placeholder': 'Estimated schedule, testing timeline, or specific export documentation needed.'
            }),
            'sample_request': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-emerald-500 bg-slate-900 border-slate-700 rounded focus:ring-slate-500'
            }),
            'consent': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-slate-400 bg-slate-900 border-slate-700 rounded focus:ring-slate-500',
                'required': 'required'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_active=True)
        self.fields['product'].empty_label = "Select from Catalog (or specify below)"
        self.fields['consent'].required = True

    def clean_website_check(self):
        val = self.cleaned_data.get('website_check')
        if val:
            raise forms.ValidationError("Automated submission detected.")
        return val

    def clean_technical_file(self):
        file = self.cleaned_data.get('technical_file')
        if file:
            max_mb = 10
            if file.size > max_mb * 1024 * 1024:
                raise forms.ValidationError(f"File size cannot exceed {max_mb} MB.")
            valid_exts = ['.pdf', '.doc', '.docx', '.txt', '.png', '.jpg', '.jpeg']
            import os
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in valid_exts:
                raise forms.ValidationError("Supported formats: PDF, DOC, DOCX, TXT, PNG, JPG.")
        return file
