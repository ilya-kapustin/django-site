from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .serializers import ShopsGroupSerializer, ShopsSerializer
from ..models import ShopsGroup, Shops


class ShopsGroupListAPIView(ListAPIView):
    '''
    Первым атребутом он принимает serializer_class,
    который мы импартируем из serializers.py.
    Данное представление будет использовать этот serializer,
    пропускать через него все данные, которые приходят.
    queryset принимает модель, которыю мы используем
    '''
    serializer_class = ShopsGroupSerializer
    queryset = ShopsGroup.objects.all()


class ShopsListAPIView(ListAPIView):
    '''
    Первым атребутом он принимает serializer_class,
    который мы импартируем из serializers.py.
    Данное представление будет использовать этот serializer,
    пропускать через него все данные, которые приходят.
    queryset принимает модель, которыю мы используем.
    filter_backends и search_fields реализуют фильтрацию.
    '''
    serializer_class = ShopsSerializer
    queryset = Shops.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
