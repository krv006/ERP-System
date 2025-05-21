from rest_framework.serializers import ModelSerializer

from students.models import StudentJourney, Language, Student, Address, PaymentDiscount, PaymentPlan, StudentPayment
from users.serializers import UserDetailModelSerializer


class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserDetailModelSerializer(instance.user).data if instance.user else None
        repr['address'] = AddressModelSerializer(instance.address).data if instance.address else None
        return repr


class StudentJourneyModelSerializer(ModelSerializer):
    class Meta:
        model = StudentJourney
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['student'] = StudentModelSerializer(instance.user).data if instance.user else None
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
        fields = 'id', 'language', 'language_level', 'certificate_name', 'certificate_score', 'user',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserDetailModelSerializer(instance.user).data if instance.user else None
        return repr


class AddressModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = 'country', 'region', 'city', 'street', 'district', 'house_number', 'postal_code'


class PaymentPlanModelSerializer(ModelSerializer):
    class Meta:
        model = PaymentPlan
        fields = 'name', 'base_amount',


class PaymentDiscountModelSerializer(ModelSerializer):
    class Meta:
        model = PaymentDiscount
        fields = 'plan', 'discount_percent', 'updated_at',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['plan'] = PaymentPlanModelSerializer(instance.plan).data if instance.plan else None
        return repr


class StudentPaymentModelSerializer(ModelSerializer):
    class Meta:
        model = StudentPayment
        fields = 'id', 'student', 'plan', 'paid_amount', 'due_date', 'is_paid', 'paid_at', 'payment_note',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['student'] = StudentModelSerializer(instance.student).data if instance.student else None
        return repr
