from . import serializers, Person, Address, PhoneNumber, Email, BasicEmailSerializer, \
    BasicPhoneNumberSerializer, BasicAddressSerializer, AddressSerializer, PhoneNumberSerializer, EmailSerializer


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
        )


class CreatePersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    addresses = BasicAddressSerializer(many=True, required=False)
    phone_numbers = BasicPhoneNumberSerializer(many=True)
    emails = BasicEmailSerializer(many=True)

    def create(self, validated_data):
        person = Person(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            date_of_birth=validated_data.get('date_of_birth'),
        )

        person.save()

        phone_number_objects = self.create_phone_numbers(validated_data.get('phone_numbers'), person)
        email_objects = self.create_emails(validated_data.get('emails'), person)
        address_objects = []

        if validated_data.get('addresses'):
            address_objects = self.create_addresses(validated_data.get('addresses'), person)

        return {
            'id': person.id,
            'first_name': person.first_name,
            'last_name': person.last_name,
            'date_of_birth': person.date_of_birth,
            'addresses': address_objects,
            'phone_numbers': phone_number_objects,
            'emails': email_objects
        }

    def create_addresses(self, address_data, person):
        addresses = [Address(**address, person=person) for address in address_data]
        address_objects = Address.objects.bulk_create(addresses)
        return address_objects

    def create_phone_numbers(self, phone_number_data, person):
        phone_numbers = [PhoneNumber(**phone_number, person=person) for phone_number in phone_number_data]
        phone_number_objects = PhoneNumber.objects.bulk_create(phone_numbers)
        return phone_number_objects

    def create_emails(self, email_data, person):
        emails = [Email(**email, person=person) for email in email_data]
        email_objects = Email.objects.bulk_create(emails)
        return email_objects


class PersonListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    date_of_birth = serializers.DateField()
    addresses = AddressSerializer(many=True, read_only=True)
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('phone_numbers').prefetch_related('emails').prefetch_related(
            'addresses').order_by('first_name')
        return queryset

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'addresses',
            'phone_numbers',
            'emails'
        )