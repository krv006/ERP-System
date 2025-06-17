from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, Serializer

from users.gen_code import generate_code
from users.models import User
from users.task import send_verification_email


class RegisterUserModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'email', 'first_name', 'last_name', 'password', 'confirm_password',

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError('Passwords did not match!')
        attrs['password'] = make_password(password)
        if not attrs.get('username'):
            attrs['username'] = attrs.get('email')
        return attrs

    def create(self, validated_data):
        user = super().create(validated_data)
        code = generate_code()
        cache.set(f"{user.email}_verification", code, timeout=120)
        send_verification_email.delay(user.email, code)
        return user


class LoginUserModelSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Bunday email mavjud emas bizda")

        if not user.check_password(password):
            raise ValidationError("Password ni xato kiritdingiz !!!")
        if not user.is_active:
            user.is_active = True
            user.save(update_fields=['is_active'])
        attrs['user'] = user
        return attrs


class VerifyCodeSerializer(Serializer):
    email = EmailField()
    code = CharField(write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs.get('email')
        code = attrs.pop('code')
        gen_code = cache.get(f'{email}_verification')
        if gen_code is None:
            raise ValidationError("Your verification already expired!")
        if code != gen_code:
            raise ValidationError("Code didn't matched")
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return user

# class ChangeUserPasswordSerializer(Serializer):
#     email = EmailField()
#     new_password = CharField(write_only=True)
#
#     def validate(self, attrs):
#         email = attrs.get('email')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             raise ValidationError("Bunday email mavjud emas bizda")


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRoleUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'role',


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email', 'role', 'first_name', 'last_name',

# todo ChangePassword

# class RessetVerifyCodeSerializer(Serializer):
#     email = EmailField()
#
#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#         email = attrs.get('email')
#         if cache.get(f"{email}_verification"):
#             raise ValidationError('Your old password is active still!')
#         code = generate_code()
#         cache.set(f"{email}_verification", code, timeout=120)
#         send_verification_email(email, code)
#         return attrs
#
#
# class ResetPasswordSerializer(Serializer):
#     email = EmailField(required=False, allow_blank=True, allow_null=True)
#     phone = CharField(required=False, allow_blank=True, allow_null=True)
#     user = HiddenField(default=CurrentUserDefault())
#
#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#         email = attrs.get('email')
#         phone_number = attrs.get('phone')
#         if not email and not phone_number:
#             raise ValidationError("Email or phone on of them are required")
#         if email:
#             if not User.objects.filter(email=email).exists():
#                 raise ValidationError(f"No such user with email: {email}")
#             code = generate_code()
#             cache.set(f"{email}_verification", code, timeout=120)
#             send_verification_email(email, code)
#         if phone_number:
#             if not User.objects.filter(phone_number=phone_number).exists():
#                 raise ValidationError(f"No such user with phone number: {phone_number}")
#             code = generate_code()
#             cache.set(f"{phone_number}_verification", code, timeout=120)
#             send_verification_phone(phone_number, code)
#         return attrs
#
#
# class ConfirmPasswordSerializer(Serializer):
#     email = EmailField(required=False, allow_blank=True, allow_null=True)
#     phone_number = CharField(required=False, allow_blank=True, allow_null=True)
#     password = CharField()
#     confirm_password = CharField()
#     code = CharField()
#
#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#         email = attrs.get("email")
#         code = attrs.pop("code")
#         phone_number = attrs.get("phone_number")
#         password = attrs.get("password")
#         confirm_password = attrs.pop("confirm_password")
#         gen_code_email = cache.get(f'{email}_verification')
#         gen_code_phone = cache.get(f'{phone_number}_verification')
#         if email:
#             if gen_code_email is None:
#                 raise ValidationError("Your verification already expired!")
#             if code != gen_code_email:
#                 raise ValidationError("Code didn't matched")
#         if phone_number:
#             if gen_code_phone is None:
#                 raise ValidationError("Your verification already expired!")
#             if code != gen_code_phone:
#                 raise ValidationError("Code didn't matched")
#         if password != confirm_password:
#             raise ValidationError("Passwords didn't matched!")
#         instance = User.objects.get(email=email) if email else User.objects.get(phone_number=phone_number)
#         instance.set_password(password)
#         instance.save()
#         return instance
