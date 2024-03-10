from rest_framework import serializers


def validate_supplier(supplier, category, manufactury):
    if (supplier is not None) and (category == manufactury):
        raise serializers.ValidationError("У завода не может быть поставщика")
