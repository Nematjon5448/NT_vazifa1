from rest_framework import serializers


class MuallifSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    familiya = serializers.CharField(max_length=50)
    tugilgan_sana = serializers.DateField()
    rasm = serializers.ImageField(required=False)

class NashriyotSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nomi = serializers.CharField(max_length=200)
    manzil = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    telefon = serializers.CharField(max_length=13)

class KitobSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nomi = serializers.CharField(max_length=150)
    janr = serializers.CharField(max_length=100)
    chop_etilgan_sana = serializers.DateField()
    rasm = serializers.ImageField(required=False)
    muallif_id = serializers.IntegerField()
    nashriyot_id = serializers.IntegerField()