from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from .serializer import ComentariosSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
