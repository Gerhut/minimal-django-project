from django import views
from django.http import HttpResponse, JsonResponse
from .models import Model

# Create your views here.
class InstancesView(views.View):
    def post(self, request):
        instance = Model(field=request.POST['field'])
        instance.save()
        return JsonResponse(instance.to_dict(), status=201)

class InstanceView(views.View):
    def get(self, request, pk):
        try:
            instance = Model.objects.get(pk=pk)
            return JsonResponse(instance.to_dict())
        except Model.DoesNotExist:
            return HttpResponse(status=404)

    def delete(self, request, pk):
        try:
            Model.objects.get(pk=pk).delete()
            return HttpResponse(status=204)
        except Model.DoesNotExist:
            return HttpResponseNotFound()
