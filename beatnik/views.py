from rest_framework.views import APIView
from .models import Music
from .serializers import MusicSerializer

class Music(APIView):
    def get(self, request, format=None):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        print(request.query_params.get('q', None))
        return Response(serializer.data)
