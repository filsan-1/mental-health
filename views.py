from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MoodLog, SessionSummary
from .serializers import MoodLogSerializer, SessionSummarySerializer

class MoodLogView(APIView):
    def get(self, request):
        logs = MoodLog.objects.filter(user=request.user)
        serializer = MoodLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MoodLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionSummaryView(APIView):
    def get(self, request):
        summaries = SessionSummary.objects.filter(provider=request.user)
        serializer = SessionSummarySerializer(summaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
