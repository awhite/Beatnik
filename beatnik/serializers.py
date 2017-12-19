from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('type', 'name', 'artist', 'album', 'apple_url', 'gpm_url', 'soundcloud_url', 'spotify_url', 'match_rating', 'insertion_date', 'update_date', 'artwork')
