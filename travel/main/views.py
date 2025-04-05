from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Klass, Mehmonxona, Travel
from .serializers import KlassSerializer, MehmonxonaSerializer, TravelSerializer


class KlassAPI(APIView):
    def get(self, request):
        try:
            klass = Klass.objects.all()
            serializer = KlassSerializer(klass, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def post(self, request):
        try:
            serializer = KlassSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            klass = Klass.objects.create(
                nomi=serializer.validated_data.get('nomi'),
                narxi=serializer.validated_data.get('narxi')
            )
            return Response(model_to_dict(klass))
        except Exception as e:
            return Response(str(e), status=404)

class KlassDetailAPI(APIView):
    def get(self, request, pk):
        try:
            klass = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(klass)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def put(self, request, pk):
        try:
            klass = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            klass.nomi = serializer.validated_data.get('nomi', klass.nomi)
            klass.narxi = serializer.validated_data.get('narxi', klass.narxi)
            klass.save()
            return Response(KlassSerializer(klass).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            klass = Klass.objects.get(pk=pk)
            klass.delete()
            return Response({'message': 'Success'})
        except Exception as e:
            return Response(str(e), status=404)

class MehmonxonaAPI(APIView):
    def get(self, request):
        try:
            mehmonxona = Mehmonxona.objects.all()
            serializer = MehmonxonaSerializer(mehmonxona, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def post(self, request):
        try:
            serializer = MehmonxonaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            mehmonxona = Mehmonxona.objects.create(
                nomi=serializer.validated_data.get('nomi'),
                yulduzlar_soni=serializer.validated_data.get('yulduzlar_soni'),
                narxi=serializer.validated_data.get('narxi')
            )
            return Response(model_to_dict(mehmonxona))
        except Exception as e:
            return Response(str(e), status=404)

class MehmonxonaDetailAPI(APIView):
    def get(self, request, pk):
        try:
            mehmonxona = Mehmonxona.objects.get(pk=pk)
            serializer = MehmonxonaSerializer(mehmonxona)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def put(self, request, pk):
        try:
            mehmonxona = Mehmonxona.objects.get(pk=pk)
            serializer = MehmonxonaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            mehmonxona.nomi = serializer.validated_data.get('nomi', mehmonxona.nomi)
            mehmonxona.yulduzlar_soni = serializer.validated_data.get('yulduzlar_soni', mehmonxona.yulduzlar_soni)
            mehmonxona.narxi = serializer.validated_data.get('narxi', mehmonxona.narxi)
            mehmonxona.save()
            return Response(MehmonxonaSerializer(mehmonxona).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            mehmonxona = Mehmonxona.objects.get(pk=pk)
            mehmonxona.delete()
            return Response({'message': 'Success'})
        except Exception as e:
            return Response(str(e), status=404)

class TravelAPI(APIView):
    def get(self, request):
        try:
            travel = Travel.objects.all()
            serializer = TravelSerializer(travel, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def post(self, request):
        try:
            serializer = TravelSerializer(data=request.data)
            serializer.is_valid()
            travel = Travel.objects.create(
                nomi=serializer.validated_data.get('nomi'),
                izoh=serializer.validated_data.get('izoh'),
                muddati=serializer.validated_data.get('muddati'),
                narxi=serializer.validated_data.get('narxi'),
                klass=serializer.validated_data.get('klass'),
                mehmonxona=serializer.validated_data.get('mehmonxona')
            )
            return Response(model_to_dict(travel))
        except Exception as e:
            return Response(str(e), status=404)

class TravelDetailAPI(APIView):
    def get(self, request, pk):
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(travel)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def put(self, request, pk):
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            travel.nomi = serializer.validated_data.get('nomi', travel.nomi)
            travel.izoh = serializer.validated_data.get('izoh', travel.izoh)
            travel.muddati = serializer.validated_data.get('muddati', travel.muddati)
            travel.narxi = serializer.validated_data.get('narxi', travel.narxi)
            travel.klass = serializer.validated_data.get('klass', travel.klass)
            travel.mehmonxona = serializer.validated_data.get('mehmonxona', travel.mehmonxona)
            travel.save()
            return Response(TravelSerializer(travel).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({'message': 'Success'})
        except Exception as e:
            return Response(str(e), status=404)