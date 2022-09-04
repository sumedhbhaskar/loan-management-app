"""
Serializers for Loan app
"""

from rest_framework import serializers
from .models import Loan, LoanApplication
from user.models import User


class LoanSerializers(serializers.ModelSerializer):
    """serializers for Loan model"""

    class Meta:
        model = Loan
        fields = "__all__"

class LoanApplicationSerializers(serializers.ModelSerializer):
    """serializers for Loan application"""

    user = serializers.PrimaryKeyRelatedField(many=False,queryset=User.objects.all())

    class Meta:
        model = LoanApplication
        fields = ['user','loan','age','gender','address','aadhaar']
        read_only_fields = ['user']



class LoanValidateSerializers(serializers.ModelSerializer):
    """
    serializers for the status of loan
    The only editable values here are status and comment in loan application, user is picked from request.user  
    """

    class Meta:
        model = LoanApplication
        fields = ['user','loan','age','gender','address','aadhaar','status','comments']
        read_only_fields = ['user','loan','age','gender','address','aadhaar']
        