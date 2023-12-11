from rest_framework import generics
from .serializers import ListCreateCatSerializer, CatSerializer, CatDeleteSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Cat


class CatListCreateView(generics.ListCreateAPIView):
    """
    Представление для вывода списка питомцев и добавления новых.
    """
    serializer_class = ListCreateCatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CatChangeView(generics.UpdateAPIView):
    """
    Представление для изменения данных питомца.
    """
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    queryset = Cat.objects.all()

    lookup_field = 'pk'

class CatDeleteView(generics.DestroyAPIView):
    """
    Удаление питомца из списка.
    """
    serializer_class = CatDeleteSerializer
    permission_classes = [IsAuthenticated]

    queryset = Cat.objects.all()

class CatView(generics.RetrieveAPIView):
    """
    Представление полного описания питомца.
    """
    serializer_class = CatSerializer
    permission_classes = [IsAuthenticated]

    queryset = Cat.objects.all()

    lookup_field = 'pk'

