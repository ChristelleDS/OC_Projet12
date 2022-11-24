from django_filters import rest_framework as filters
from .models import Contract


class ContractFilter(filters.FilterSet):
    client = filters.CharFilter(field_name="client__lastname",
                                    lookup_expr="icontains")
    salescontact = filters.CharFilter(field_name="salescontact__email",
                                   lookup_expr="icontains")
    status = filters.BooleanFilter(field_name="status",
                               lookup_expr="iexact")

    class Meta:
        model = Contract
        fields = ["client", "salescontact", "status"]