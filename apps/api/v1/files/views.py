from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import CodeFileSerializer, CodeFile, CodeFileRetrieveSerializer


class CodeFileViewSet(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer


class CodeFileDetailView(RetrieveAPIView):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileRetrieveSerializer
