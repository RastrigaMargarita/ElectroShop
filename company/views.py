from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from company.models import Company, Town, Country
from company.serializer import CompanySerializer, CountrySerializer, TownSerializer
from user.permissions import IsActive


class CompanyViewSet(ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def list(self, request, *args, **kwargs):
        country_parameter = self.request.query_params.get('country')
        if country_parameter is None:
            queryset = Company.objects.all()
        else:
            queryset = Company.objects.filter(country=country_parameter)
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


class CountryViewSet(ModelViewSet):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class TownViewSet(ModelViewSet):

    serializer_class = TownSerializer
    queryset = Town.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
