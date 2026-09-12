from datetime import datetime

def site_settings(request):
    return {
        'SITE_NAME': 'STELLAR SHIPERS',
        'SITE_LEGAL_NAME': 'STELLAR SHIPERS',
        'SITE_TAGLINE': 'WHERE TRUST MEETS VALUE.',
        'SITE_SUPPORTING_LINE': 'Indian sourcing. International standards. Responsible export coordination.',
        'SITE_SUBTITLE': 'India-based international sourcing and export company connecting carefully selected Indian producers with global B2B buyers.',
        'PRIMARY_EMAIL': 'stellarshipper45@gmail.com',
        'PRIMARY_PHONE': 'Available upon inquiry / B2B RFQ',
        'SUPPLIER_LOCATION': 'Jalgaon, Maharashtra, India',
        'PRIMARY_MARKET': 'Europe (with initial focus on Germany and France)',
        'PRIMARY_CUSTOMER': 'Textile manufacturers and natural-fiber distributors',
        'CURRENT_YEAR': datetime.now().year,
        'TRUST_PILLARS': [
            {
                'title': 'Trust',
                'subtitle': 'Non-Negotiable',
                'desc': 'No untested numbers presented as certified data. What we agree upon is what arrives at your destination.',
                'icon': 'shield'
            },
            {
                'title': 'Premium Value',
                'subtitle': 'Reliability & Excellence',
                'desc': 'We compete on value, consistent grading and reliability—not on being the cheapest supplier.',
                'icon': 'gem'
            },
            {
                'title': 'International Professionalism',
                'subtitle': 'Disciplined Coordination',
                'desc': 'Clear B2B communication, disciplined export documentation, and dependable maritime coordination.',
                'icon': 'globe'
            }
        ]
    }
