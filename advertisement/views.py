from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement.models import Ad
from advertisement.serializers import AdSerializer


class AdvertisementView(APIView):
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

    # @login_required(login_url='/login')
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response(status=400)
        ad = Ad()
        ad.title = title
        ad.content = content
        ad.save()
        return Response(data={'id': ad.id}, status=201)

    def delete(self, request, ad_id):
        if not Ad.objects.filter(id=ad_id).exists():
            return Response(status=404)
        Ad.objects.filter(id=ad_id).delete()
        return Response(status=200)