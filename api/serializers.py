from rest_framework import serializers
from topy.models import *

#UserType
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


#Activity
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

#User details
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Senior citizen details
class SeniorCitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeniorCitizen
        fields = '__all__'


#Child details
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

#Pet details
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

#TOPYStation
class TOPYStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOPYStation
        fields = '__all__'

#Match details
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trialuser
#         fields = '__all__'
