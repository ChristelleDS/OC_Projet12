from django_filters import rest_framework as filters
from .models import Client


class ClientFilter(filters.FilterSet):
    firstname = filters.CharFilter(field_name="firstname",
                                    lookup_expr="icontains")
    lastname = filters.CharFilter(field_name="lastname",
                                   lookup_expr="icontains")
    email = filters.CharFilter(field_name="email",
                               lookup_expr="iexact")
    company = filters.CharFilter(field_name="company",
                               lookup_expr="icontains")
    qualification = filters.CharFilter(field_name="qualification",
                                 lookup_expr="iexact")

    class Meta:
        model = Client
        fields = ["firstname", "lastname", "email", "company", "qualification"]