content_part3 = '''
<!-- 4. FEATURED PRODUCT — RAW BANANA FIBER (Page 5 & 15) -->
<section class="py-20 bg-[#161A1E] border-b border-[#353B44]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
            <div class="space-y-2 max-w-2xl">
                <div class="inline-flex items-center space-x-2 text-xs font-mono uppercase tracking-widest text-[#9AA0A6]">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    <span>Initial Featured Product</span>
                </div>
                <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">Textile-Grade Raw Banana Fiber</h2>
                <p class="text-slate-300 text-sm leading-relaxed">
                    Natural, mechanically extracted and dried banana fiber sourced from G9 banana pseudostems, supplied in cleaned/combed fiber bundles for textile and natural-fiber applications.
                </p>
            </div>
            <div class="mt-4 md:mt-0 shrink-0">
                <a href="{% url 'products:detail' 'banana-fiber' %}" class="text-xs uppercase tracking-widest font-mono text-slate-300 hover:text-white flex items-center space-x-1">
                    <span>Full Product Data Sheet</span>
                    <span>&rarr;</span>
                </a>
            </div>
        </div>

        <div class="bg-[#1E2328] border border-[#353B44] rounded-xl overflow-hidden shadow-xl">
            <div class="grid grid-cols-1 lg:grid-cols-12">
                <div class="lg:col-span-7 p-6 sm:p-10 space-y-6">
                    <div class="flex flex-wrap items-center gap-2">
                        <span class="badge-stated px-3 py-1 rounded text-xs font-mono font-semibold">SUPPLIER-STATED & CONFIRMED PARAMETERS</span>
                        <span class="badge-pending px-3 py-1 rounded text-xs font-mono font-semibold">LAB TESTING CONDUCTED PER BUYER SPEC</span>
                    </div>

                    <div class="border border-[#353B44] rounded-lg overflow-hidden text-xs font-mono">
                        <table class="w-full text-left">
                            <thead class="bg-[#161A1E] text-slate-400 border-b border-[#353B44] uppercase tracking-wider text-[11px]">
                                <tr>
                                    <th class="py-2.5 px-4">Parameter</th>
                                    <th class="py-2.5 px-4">Current Information</th>
                                    <th class="py-2.5 px-4 text-right">Status</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-[#2D333B] bg-[#1E2328] text-slate-300">
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Banana Variety</td>
                                    <td class="py-2.5 px-4">G9 (commonly associated with Grand Naine)</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">Supplier-stated</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Raw Material</td>
                                    <td class="py-2.5 px-4">Musa plant pseudostems</td>
                                    <td class="py-2.5 px-4 text-right text-emerald-400 font-semibold">Confirmed</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Extraction Method</td>
                                    <td class="py-2.5 px-4">Mechanical decortication</td>
                                    <td class="py-2.5 px-4 text-right text-emerald-400 font-semibold">Confirmed</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Post-Extraction Processing</td>
                                    <td class="py-2.5 px-4">Drying only</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">Supplier-stated</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Chemical Treatment</td>
                                    <td class="py-2.5 px-4">No chemical treatment / 100% natural</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">Supplier-stated</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Typical Fiber Length</td>
                                    <td class="py-2.5 px-4">Approx. 4–5 ft</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">Supplier-stated</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Colour</td>
                                    <td class="py-2.5 px-4">Golden</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">Visually apparent</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Tensile Strength & Fineness</td>
                                    <td class="py-2.5 px-4 text-amber-300">No generic numbers published; tested upon buyer order</td>
                                    <td class="py-2.5 px-4 text-right text-amber-300">Testing on-demand</td>
                                </tr>
                                <tr>
                                    <td class="py-2.5 px-4 text-white font-semibold">Moisture & Batch Consistency</td>
                                    <td class="py-2.5 px-4">Natural variation expected; conditioned before dispatch</td>
                                    <td class="py-2.5 px-4 text-right text-slate-400">QC tolerance</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div>
                        <div class="text-xs uppercase tracking-wider text-[#9AA0A6] font-mono mb-2">Potential Applications & Uses (Subject to buyer specification):</div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono text-slate-300">
                            <div class="p-2.5 bg-[#161A1E] rounded border border-[#2D333B]">&bull; Natural-fiber textile development</div>
                            <div class="p-2.5 bg-[#161A1E] rounded border border-[#2D333B]">&bull; Blended yarn / textile development</div>
                            <div class="p-2.5 bg-[#161A1E] rounded border border-[#2D333B]">&bull; Woven or nonwoven materials</div>
                            <div class="p-2.5 bg-[#161A1E] rounded border border-[#2D333B]">&bull; Home-textiles & furnishing</div>
                            <div class="p-2.5 bg-[#161A1E] rounded border border-[#2D333B] sm:col-span-2">&bull; Craft, specialty and technical natural-fiber uses</div>
                        </div>
                    </div>

                    <div class="pt-2 flex flex-wrap gap-4">
                        <a href="{% url 'products:detail' 'banana-fiber' %}" class="metallic-silver-btn px-6 py-3 rounded text-xs uppercase tracking-wider font-semibold">
                            Full Technical Data Sheet
                        </a>
                        <a href="{% url 'rfq:submit' %}?product=banana-fiber&sample=1" class="px-6 py-3 rounded text-xs uppercase tracking-wider font-semibold border border-[#4A5563] bg-[#252A30] hover:bg-[#2F363F] text-white transition-colors">
                            Request Fiber Sample
                        </a>
                    </div>
                </div>

                <div class="lg:col-span-5 bg-[#161A1E] p-6 sm:p-10 border-t lg:border-t-0 lg:border-l border-[#353B44] flex flex-col justify-between space-y-6">
                    <div class="space-y-4">
                        <span class="text-xs font-mono uppercase tracking-wider text-[#9AA0A6]">Current Commercial Parameters</span>
                        
                        <div class="space-y-3 text-xs font-mono">
                            <div class="p-3 rounded bg-[#1E2328] border border-[#2D333B]">
                                <div class="text-slate-400 uppercase text-[10px]">Supplier Origin Location</div>
                                <div class="text-white font-semibold mt-1 font-sans">Jalgaon, Maharashtra, India</div>
                            </div>

                            <div class="p-3 rounded bg-[#1E2328] border border-[#2D333B]">
                                <div class="text-slate-400 uppercase text-[10px]">Supplier Minimum Order Quantity (MOQ)</div>
                                <div class="text-white font-semibold mt-1 font-sans">500 kg (expandable to full container load)</div>
                            </div>

                            <div class="p-3 rounded bg-[#1E2328] border border-[#2D333B]">
                                <div class="text-slate-400 uppercase text-[10px]">Monthly Production Capacity</div>
                                <div class="text-white font-semibold mt-1 font-sans">5–10 MT / month (stated as expandable)</div>
                            </div>

                            <div class="p-3 rounded bg-[#1E2328] border border-[#2D333B]">
                                <div class="text-slate-400 uppercase text-[10px]">Packaging</div>
                                <div class="text-white font-semibold mt-1 font-sans">Polythene / poly-woven wraps for long-distance export transport</div>
                            </div>

                            <div class="p-3 rounded bg-[#1E2328] border border-[#2D333B]">
                                <div class="text-slate-400 uppercase text-[10px]">Pricing Structure</div>
                                <div class="text-slate-200 mt-1 font-sans">Quoted on RFQ based on required quantity, destination port & Incoterms (No fixed public retail price)</div>
                            </div>
                        </div>
                    </div>

                    <div class="p-4 rounded bg-[#1E2328] border border-amber-800/40 text-xs text-amber-200/90 font-mono">
                        Notice: We do not publish unverified numbers as certified data. Lot testing is coordinated directly with independent testing bodies upon buyer specification.
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>
'''
with open('templates/pages/home.html', 'a', encoding='utf-8') as f:
    f.write(content_part3)
