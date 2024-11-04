from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets

from base.models import Item
from api.serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer(queryset, many=True)
    return Response(serializer_class.data)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
