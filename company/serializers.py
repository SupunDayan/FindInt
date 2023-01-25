from rest_framework import serializers
from company.models import company


class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ['id','name','location','description','email']