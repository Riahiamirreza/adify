from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement.models import Ad
from advertisement.serializers import AdSerializer


class AdvertisementView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, ad_id=None):
        try:
            if ad_id is None:
                limit = int(request.query_params.get('limit', '10'))
                offset = int(request.query_params.get('offset', '0'))
                qs = Ad.objects.all()[offset:offset+limit]
                return Response(AdSerializer(qs, many=True).data)
            if not (qs := Ad.objects.filter(id=ad_id).all()).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            ad = qs.get()
            return Response(AdSerializer(ad).data)
        except Exception as exc:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response(status=400)
        ad = Ad()
        ad.title = title
        ad.content = content
        ad.author = request.user
        ad.save()
        return Response(data={'id': ad.id}, status=201)

    def delete(self, request, ad_id):
        try:
            if not (qs := Ad.objects.filter(id=ad_id)).exists():
                return Response(status=404)
            ad = qs.get()
            if ad.author.id != request.user.id:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            Ad.objects.filter(id=ad_id).delete()
            return Response(status=200)
        except Exception as exc:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
