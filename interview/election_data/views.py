from typing import Any, Dict
from django.views.generic import ListView, DetailView, TemplateView
from .models import AgentName, PollingUnit, Lga, AnnouncedPuResult

class PollingUnitsList(ListView):
    template_name = 'polling-units.html'
    queryset = PollingUnit.objects.all()

class PollingUnitDetailView(DetailView):
    model = PollingUnit
    template_name = 'polling-unit-detail.html'
    context_object_name = 'polling_unit'

class LGAResultView(TemplateView):
    template_name = 'lga-result-total.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        kwargs.update(**self.get_lgas())
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        kwargs.update(**self.get_lgas())
        lga_id = request.POST.get('local_government')

        pollingunit_for_lga = PollingUnit.objects.filter(
            lga_id =lga_id,
        )
        if pollingunit_for_lga.exists():
            score = self.pollingUnit_sum(pollingunit_for_lga)
            kwargs['total_score'] = score
        else:
            kwargs['total_score'] = 0

        single_lga_item = Lga.objects.get(lga_id=lga_id)
        kwargs['selected_local_government'] = single_lga_item

        return super().render_to_response(context=kwargs) 
       
    def get_lgas(self, **kwargs):
        kwargs['local_governments'] = Lga.objects.all()
        return kwargs
    

    def pollingUnit_sum(self, polling_unit):
        # store the id's 
        polling_unit_ids = [poll.uniqueid for poll in polling_unit]


        announced_pu_query = AnnouncedPuResult.objects.filter(
            polling_unit_uniqueid__in=polling_unit_ids
        )

        party_scores = [score.party_score for score in announced_pu_query]
        return sum(party_scores)
