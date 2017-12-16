from rest_framework import viewsets, generics, mixins
from addresses.serializers import *
from addresses.models import *





class CreatePersonView(generics.CreateAPIView):

    serializer_class = CreatePersonSerializer


class PeopleViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = PersonListSerializer

    def get_queryset(self):
        if self.request.query_params.get('qt'):
            qt = self.request.query_params.get('qt')
            queryset = Person.objects.filter(first_name__icontains=qt) | Person.objects.filter(last_name__icontains=qt)
            queryset = self.get_serializer_class().setup_eager_loading(queryset)
        else:
            queryset = Person.objects.all()
            queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class AddressViewSet(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):

    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class EmailViewSet(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = EmailSerializer

