from rest_framework.serializers import ModelSerializer

from students.models import StudentJourney, Language
from users.serializers import UserDetailModelSerializer


class StudentJourneyModelSerializer(ModelSerializer):
    class Meta:
        model = StudentJourney
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserDetailModelSerializer(instance.user).data if instance.user else None
        return repr


class StudentJourneyInJobModelSerializer(ModelSerializer):
    class Meta:
        model = StudentJourney
        fields = 'id', 'job_offer_accepted',


class StudentJourneyStatusUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = StudentJourney
        fields = 'id', 'status',


class LanguageModelSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = 'id', 'language', 'language_grid', 'user',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserDetailModelSerializer(instance.user).data if instance.user else None
        return repr
