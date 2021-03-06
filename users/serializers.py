from rest_framework import serializers
from .models import User, User_status, UserReview


class UserFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "profile_pic",
            "first_name",
            "reg_number",
            "hostel_room",
            "phone",
            "gender"
        )


'''
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
'''
    
class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "reg_number",
            "hostel_room",
            "phone",
            "profile_pic"
        )
        


class UserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_status
        fields = (
            "deliveries_done"
        )

class UserInfoSerializer(serializers.ModelSerializer):
    user_status = UserStatusSerializer(read_only = True)

    class Meta:
        model = User
        fields = (
            "profile_pic",
            "first_name",
            "reg_number",
            "phone",
            "email",
            "total_tasks",
            "completed_tasks",
            "uncompleted_tasks",
            "user_status"
        )


class AverageReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_status
        fields = (
            "average_review",
            "deliveries_done"
        )


class AverageReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = (
            "review_star",
            "review_text"
        )


class IndividualUserSerializer(serializers.ModelSerializer):
    user_status = AverageReviewSerializer(read_only = True)
    user_review = AverageReviewDetailSerializer(many = True, read_only = True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "reg_number",
            "profile_pic",
            "total_tasks",
            "completed_tasks",
            "uncompleted_tasks",
            "user_status",
            "user_review"
        )

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "profile_pic"
        )