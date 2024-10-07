from rest_framework import serializers
from .models import login,Event
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields=('name','roll','cls','plc','dplc','prb','img')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('eve', 'venue', 'DT', 'contact', 'poster')