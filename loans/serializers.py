from rest_framework import serializers
from copys.serializers import CopySerializer
from .models import Loan

import ipdb

class LoansSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Loan:
        return Loan.objects.create(**validated_data)
    
    def update(self, instance: Loan, validated_data: dict) -> Loan:
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
    
    copy = CopySerializer(read_only=True)
    
    class Meta:
        model = Loan
        fields= [
            "id",
            "borrowed_date",
            "devolution_date",
            "is_devoluted",
            "blocked_until",
            "copy",
            "user_id",
        ]
