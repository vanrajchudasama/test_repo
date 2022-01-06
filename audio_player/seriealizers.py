from rest_framework import serializers
from audio_player.models import Audio
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class AudioSeriealizer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=50)
    file = serializers.FileField()
    class Meta:
        fields = '__all__'
        model=Audio


        # this is main brance