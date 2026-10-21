from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView

from .forms import ContatoForm
from .models import Carro


class CarroListView(ListView):
    model = Carro
    template_name = "carros/vendas_carros.html"
    context_object_name = "carros"
    paginate_by = 9

    def get_queryset(self):
        qs = Carro.objects.filter(disponivel=True)
        params = self.request.GET

        q = params.get("q", "").strip()
        if q:
            qs = qs.filter(Q(marca__icontains=q) | Q(modelo__icontains=q) | Q(versao__icontains=q))

        combustivel = params.get("combustivel")
        if combustivel in Carro.Combustivel.values:
            qs = qs.filter(combustivel=combustivel)

        cambio = params.get("cambio")
        if cambio in Carro.Cambio.values:
            qs = qs.filter(cambio=cambio)

        preco_max = params.get("preco_max")
        if preco_max:
            try:
                qs = qs.filter(preco__lte=Decimal(preco_max))
            except InvalidOperation:
                pass

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # total de resultados (não só da página atual)
        ctx["total_carros"] = ctx["paginator"].count if ctx.get("paginator") else len(ctx["carros"])
        # filtros atuais, para manter na paginação
        params = self.request.GET.copy()
        params.pop("page", None)
        ctx["querystring"] = params.urlencode()
        return ctx


class CarroDetailView(DetailView):
    model = Carro
    template_name = "carros/detalhe_carro.html"
    context_object_name = "carro"

    def get_queryset(self):
        return Carro.objects.filter(disponivel=True)


@require_POST
def contato(request):
    form = ContatoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Mensagem enviada! Em breve um consultor entrará em contato.")
    else:
        messages.error(request, "Não foi possível enviar. Confira os campos e tente novamente.")

    destino = request.META.get("HTTP_REFERER") or reverse("lista")
    return redirect(destino)
