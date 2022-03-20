from rest_framework.views import APIView
from .serializers import *
from .parser import main
from rest_framework.response import Response

# Create your views here.

class ParsingView(APIView):
    def get(self, request):
        parsing = main()

        serializer = ParsingSerializer(instance=parsing, many=True)
        return Response(serializer.data)