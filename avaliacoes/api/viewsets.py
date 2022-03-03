from rest_framework.viewsets import ModelViewSet
from avaliacoes.api.serializer import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer