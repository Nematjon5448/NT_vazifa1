from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Muallif, Nashriyot, Kitob
from .serializers import MuallifSerializer, NashriyotSerializer, KitobSerializer

class MuallifAPIView(APIView):
    def get(self, request):
        muallif = Muallif.objects.all()
        serializer = MuallifSerializer(muallif, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = MuallifSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            muallif = Muallif.objects.create(
                ism=serializer.validated_data.get("ism"),
                familiya=serializer.validated_data.get("familiya"),
                tugilgan_sana=serializer.validated_data.get("tugilgan_sana"),
                rasm=serializer.validated_data.get("rasm"),
            )
            return Response(model_to_dict(muallif))
        except Exception as e:
            return Response(str(e), status=404)

class MuallifDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            muallif = Muallif.objects.get(pk=pk)
            serializer = MuallifSerializer(muallif)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=404)

    def put(self, request, pk):
        try:
            muallif = Muallif.objects.get(pk=pk)
            serializer = MuallifSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            muallif.ism = serializer.validated_data.get("ism", muallif.ism)
            muallif.familiya = serializer.validated_data.get("familiya", muallif.familiya)
            muallif.tugilgan_sana = serializer.validated_data.get("tugilgan_sana", muallif.tugilgan_sana)
            muallif.rasm = serializer.validated_data.get("rasm", muallif.rasm)
            muallif.save()
            return Response(MuallifSerializer(muallif).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            muallif = Muallif.objects.get(pk=pk)
            muallif.delete()
            return Response({"message": "Success"})
        except Exception as e:
            return Response(str(e), status=404)

class NashriyotAPIView(APIView):
    def get(self, request):
        nashriyot = Nashriyot.objects.all()
        serializer = NashriyotSerializer(nashriyot, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = NashriyotSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            nashriyot = Nashriyot.objects.create(
                nomi=serializer.validated_data.get("nomi"),
                manzil=serializer.validated_data.get("manzil"),
                email=serializer.validated_data.get("email"),
                telefon=serializer.validated_data.get("telefon")
            )
            return Response(model_to_dict(nashriyot))
        except Exception as e:
            return Response(str(e), status=404)

class NashriyotDetailAPIView(APIView):
    def get(self, request, pk):
        nashriyot = Nashriyot.objects.get(pk=pk)
        serializer = NashriyotSerializer(nashriyot)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            nashriyot = Nashriyot.objects.get(pk=pk)
            serializer = NashriyotSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            nashriyot.nomi = serializer.validated_data.get("nomi", nashriyot.nomi)
            nashriyot.manzil = serializer.validated_data.get("manzil", nashriyot.manzil)
            nashriyot.email = serializer.validated_data.get("email", nashriyot.email)
            nashriyot.telefon = serializer.validated_data.get("telefon", nashriyot.telefon)
            nashriyot.save()
            return Response(NashriyotSerializer(nashriyot).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            nashriyot = Nashriyot.objects.get(pk=pk)
            nashriyot.delete()
            return Response({"message": "Success"})
        except Exception as e:
            return Response(str(e), status=404)

class KitobAPIView(APIView):
    def get(self, request):
        kitob = Kitob.objects.all()
        serializer = KitobSerializer(kitob, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = KitobSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            kitob = Kitob.objects.create(
                nomi=serializer.validated_data.get("nomi"),
                janr=serializer.validated_data.get("janr"),
                chop_etilgan_sana=serializer.validated_data.get("chop_etilgan_sana"),
                rasm=serializer.validated_data.get("rasm"),
                muallif_id=serializer.validated_data.get("muallif_id"),
                nashriyot_id=serializer.validated_data.get("nashriyot_id"),
            )
            return Response(model_to_dict(kitob))
        except Exception as e:
            return Response(str(e), status=404)

class KitobDetailAPIView(APIView):
    def get(self, request, pk):
        kitob = Kitob.objects.get(pk=pk)
        serializer = KitobSerializer(kitob)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            kitob = Kitob.objects.get(pk=pk)
            serializer = KitobSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            kitob.nomi = serializer.validated_data.get("nomi", kitob.nomi)
            kitob.janr = serializer.validated_data.get("janr", kitob.janr)
            kitob.chop_etilgan_sana = serializer.validated_data.get("chop_etilgan_sana", kitob.chop_etilgan_sana)
            kitob.rasm = serializer.validated_data.get("rasm", kitob.rasm)
            kitob.muallif = serializer.validated_data.get("muallif", kitob.muallif)
            kitob.nashriyot = serializer.validated_data.get("nashriyot", kitob.nashriyot)
            kitob.save()
            return Response(KitobSerializer(kitob).data)
        except Exception as e:
            return Response(str(e), status=404)

    def delete(self, request, pk):
        try:
            kitob = Kitob.objects.get(pk=pk)
            kitob.delete()
            return Response({"message": "Success"})
        except Exception as e:
            return Response(str(e), status=404)