"""
Loan app views, contains
LoanViewsets -> Method POST
LoanApplicationviewsets -> Methods POST, PUT
LoanValidateviewsets -> Method GET, Update

"""

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,ListModelMixin
from .serializers import LoanSerializers,LoanApplicationSerializers, LoanValidateSerializers
from .permissions import IsSuperuser
from rest_framework.permissions import IsAuthenticated
from .models import Loan, LoanApplication
from rest_framework.response import Response
from rest_framework import status


class LoanViewsets(CreateModelMixin,UpdateModelMixin,ListModelMixin,GenericViewSet):
    """ Loan Viewset """
    serializer_class = LoanSerializers
    queryset = Loan.objects.all()
    permission_classes = [IsAuthenticated,IsSuperuser,]


class LoanApplicationViewsets(CreateModelMixin,UpdateModelMixin,GenericViewSet):
    """ Loan application viewsets """
    serializer_class = LoanApplicationSerializers
    queryset = LoanApplication.objects.all()
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        """added user.id in request"""
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoanValidateViewsets(ListModelMixin,UpdateModelMixin,GenericViewSet):
    """ Loan validate viewsets """
    serializer_class = LoanValidateSerializers
    queryset = LoanApplication.objects.all()
    permission_classes = [IsAuthenticated,IsSuperuser,]


