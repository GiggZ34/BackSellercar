from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TopStatView(APIView):
    def get(self, request, *args, **kwargs):
        print()

