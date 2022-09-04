"""
Loan app views, contains
LoanViewsets -> Method POST
LoanApplicationviewsets -> Methods POST, PUT
LoanValidateviewsets -> Method GET, Update

"""

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,ListModelMixin
from .serializers import LoanSerializers,LoanApplicationSerializers, LoanValidateSerializers
from .permissions import IsSuperuser
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Loan, LoanApplication


class LoanViewsets(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    """ Loan Viewset """
    serializer_class = LoanSerializers
    queryset = Loan.objects.all()
    permission_classes = []


class LoanApplicationViewsets(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    """ Loan application viewsets """
    serializer_class = LoanApplicationSerializers
    queryset = LoanApplication.objects.all()
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LoanValidateViewsets(ListModelMixin,UpdateModelMixin,GenericViewSet):
    """ Loan validate viewsets """
    serializer_class = LoanValidateSerializers
    queryset = LoanApplication.objects.all()
    permission_classes = []


