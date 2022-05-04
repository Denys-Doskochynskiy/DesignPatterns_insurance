from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from insurance_lab.models.insurance_data import InsuranceData

from insurance_lab.models.user import User
from insurance_lab.serializers.insurance_data_serializer import InsuranceDataSerializer
from rest_framework.response import Response


class InsuranceDataListCreateAPIView(ListCreateAPIView):
    serializer_class = InsuranceDataSerializer
    queryset = InsuranceData.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        created_response = super().create(request, *args, **kwargs)
        if created_response.get("reserved_by_user") and created_response.get("is_available") is not None:
            user_id = int(request_data.pop('reserved_by_user')[0])
            book_insurance_to_user(request_serializer, user_id)  # METHOD INJECTION
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response


def book_insurance_to_user(request_serializer, user_id):
    user_obj = User.objects.get(id=user_id)
    request_obj = request_serializer.save()
    request_obj.synk_insurance_to_user(user_obj, False)
    request_obj.save()


class InsuranceDataRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InsuranceDataSerializer
    queryset = InsuranceData.objects.all()
