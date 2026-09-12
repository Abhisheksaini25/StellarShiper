content = '''{% extends 'base.html' %}

{% block title %}{{ SITE_NAME }} | {{ SITE_TAGLINE }} - Indian Sourcing & Export Coordination{% endblock %}

{% block content %}

<!-- 1. HERO SECTION (Dark Charcoal to Black per Page 6 & 14) -->
<section class="relative overflow-hidden pt-12 pb-20 lg:pt-20 lg:pb-28 bg-[#1E2328] border-b border-[#353B44]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl space-y-6">
            <!-- Strategic Positioning Badge -->
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded border border-[#4A5563] bg-[#161A1E] text-[11px] font-mono tracking-widest text-slate-300 uppercase">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span>India-Based Sourcing & Export Company</span>
            </div>

            <!-- Suggested Homepage Headline (Page 3) -->
            <h1 class="text-4xl sm:text-6xl lg:text-7xl font-bold tracking-tight text-white uppercase font-sans leading-tight">
                WHERE TRUST <br>
                <span class="metallic-silver-text">MEETS VALUE.</span>
            </h1>

            <!-- Suggested Supporting Line (Page 3) -->
            <p class="text-lg sm:text-xl font-medium text-slate-300 font-mono tracking-wide">
                Indian sourcing. International standards. Responsible export coordination.
            </p>

            <!-- Suggested Homepage Introduction (Page 3) -->
            <p class="text-base text-slate-300 leading-relaxed max-w-2xl">
                STELLAR SHIPERS connects carefully selected Indian producers with global B2B buyers while managing sourcing, quality verification, customization and export coordination.
            </p>

            <!-- CTAs -->
            <div class="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center space-y-3 sm:space-y-0 sm:space-x-4">
                <a href="{% url 'rfq:submit' %}" class="metallic-silver-btn px-8 py-4 rounded text-xs uppercase tracking-widest font-bold text-center shadow-md">
                    Request Quote
                </a>
                <a href="{% url 'products:detail' 'banana-fiber' %}" class="px-8 py-4 rounded text-xs uppercase tracking-widest font-semibold text-center border border-[#4A5563] bg-[#252A30] hover:bg-[#2F363F] text-slate-200 transition-colors">
                    View Banana Fiber Specs
                </a>
            </div>

            <!-- Key Origin & Trade Metrics (Page 2 & 4) -->
            <div class="pt-8 grid grid-cols-2 sm:grid-cols-4 gap-4 border-t border-[#353B44] text-left text-xs font-mono">
                <div class="p-3 bg-[#161A1E] rounded border border-[#2D333B]">
                    <div class="text-slate-400 uppercase text-[10px]">Producer Origin</div>
                    <div class="text-white font-bold text-sm mt-0.5">Jalgaon, India</div>
                </div>
                <div class="p-3 bg-[#161A1E] rounded border border-[#2D333B]">
                    <div class="text-slate-400 uppercase text-[10px]">Initial Featured MOQ</div>
                    <div class="text-white font-bold text-sm mt-0.5">500 kg</div>
                </div>
                <div class="p-3 bg-[#161A1E] rounded border border-[#2D333B]">
                    <div class="text-slate-400 uppercase text-[10px]">Primary Markets</div>
                    <div class="text-white font-bold text-sm mt-0.5">Germany & France</div>
                </div>
                <div class="p-3 bg-[#161A1E] rounded border border-[#2D333B]">
                    <div class="text-slate-400 uppercase text-[10px]">Primary Customer</div>
                    <div class="text-emerald-400 font-bold text-sm mt-0.5">Textile Mills</div>
                </div>
            </div>
        </div>
    </div>
</section>
'''
with open('templates/pages/home.html', 'w', encoding='utf-8') as f:
    f.write(content)
