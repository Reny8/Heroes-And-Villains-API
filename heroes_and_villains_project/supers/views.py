from rest_framework.decorators import api_view
from .models import Super, Power
from .serializers import PowerSerializer, SuperSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from super_types.models import Super_Type

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        custom_response_dictionary = {}
        type_param = request.query_params.get('type')
        supers = Super.objects.all()

        if type_param:
            supers = supers.filter(super_type__type = type_param)
            serializer = SuperSerializer(supers,many = True)
            return Response(serializer.data)
        else:
            super_types = Super_Type.objects.all()
            for type in super_types:
                supers = Super.objects.filter(super_type_id = type.id)
                serializer = SuperSerializer(supers, many = True)
                custom_response_dictionary[type.type] = serializer.data

            return Response(custom_response_dictionary)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE','PATCH'])
def super_detail(request,pk):
    super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = SuperSerializer(super,data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
    if request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    if request.method == 'PATCH':
        serializer = SuperSerializer(super, data = request.data, partial = True)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)

