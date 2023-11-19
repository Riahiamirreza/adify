from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement.models import Ad
from advertisement.serializers import AdSerializer


class AdvertiementView(APIView):
    def get(self, request, ad_id=None):
        ad = Ad.objects.filter(id=ad_id).get()
        return Response(AdSerializer(ad).data)

    def put(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response(status=400)
        ad = Ad()
        ad.title = title
        ad.content = content
        ad.save()
        return Response(data={'id': ad.id}, status=201)
