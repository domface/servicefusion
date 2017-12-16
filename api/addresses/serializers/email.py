from . import serializers, Email

class EmailSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Email
        fields = (
            'id',
            'email',
            'person_id'
        )



class BasicEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = (
            'id',
            'email',
            'person_id'
        )
