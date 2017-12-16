from . import serializers, PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PhoneNumber
        fields = (
            'id',
            'number',
            'type',
            'person_id'
        )


class BasicPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = (
            'id',
            'number',
            'type',
            'person_id'
        )

