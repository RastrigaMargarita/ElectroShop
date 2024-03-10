from rest_framework import serializers
from company.models import Company, Country, Town


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ['debt']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = "__all__"
