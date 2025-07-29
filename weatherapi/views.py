from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_weather_data
from rest_framework import status
# Create your views here.

class WeatherApiView(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({'error' : 'City parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = get_weather_data(city)
        return Response(data)