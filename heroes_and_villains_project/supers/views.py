from rest_framework.decorators import api_view
from .models import Super
from .serializers import SuperSerializer
from rest_framework.response import Response

@api_view(['GET'])
def supers_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        serializer = SuperSerializer(super,many = True)
        return Response(serializer.data)
        