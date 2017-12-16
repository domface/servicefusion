from . import serializers, Address

class AddressSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Address
        fields = (
            'id',
            'street',
            'street_2',
            'city',
            'state',
            'zip',
            'person_id'
        )


class BasicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'street',
            'street_2',
            'city',
            'state',
            'zip',
        )