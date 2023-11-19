from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement.models import Ad
from advertisement.serializers import AdSerializer


class AdvertiementView(APIView):
    def get(self, request, ad_id=None):
        ad = Ad.objects.filter(id=ad_id)
        return Response(AdSerializer(ad).data)
