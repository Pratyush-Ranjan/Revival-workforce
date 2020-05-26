from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic
from .geocode import getCoords
from .dist import getdistance
from .forms import WorkerCreateForm
from .models import Worker
from accounts.models import Company 

class IndexView(LoginRequiredMixin,generic.ListView):
	template_name = 'workforce/index.html'
	model = Worker

	#function to fetch the queryset
	def get_queryset(self):
		queryset = Worker.objects.filter(created_by=self.request.user)
		return queryset

class CreateWorker(LoginRequiredMixin,generic.CreateView):
    #python method corresponding to a get request
    def get(self, request, *args, **kwargs):
        context = {'wform': WorkerCreateForm()}
        return render(request, 'workforce/create.html', context)
    def post(self, request, *args, **kwargs):
        form = WorkerCreateForm(request.POST)
        if form.is_valid():
            worker = Worker()
            worker.Firstname = request.POST.get('Firstname')
            worker.Lastname = request.POST.get('Lastname')
            worker.created_by = request.user
            worker.Phone_no = request.POST.get('Phone_no')
            worker.Address = request.POST.get('Address')
            worker.Industry = request.POST.get('Industry')
            worker.Skill = request.POST.get('Skill')
            worker.Aadhaar = request.POST.get('Aadhaar')
            worker.PAN = request.POST.get('PAN')
            worker.save()
            return HttpResponseRedirect("/home")
        else:
            return render(request, 'workforce/create.html', {'wform': form})
        
class JobSearch(LoginRequiredMixin,generic.View):
    def get(self, request, *args, **kwargs):
        worker = Worker.objects.get(id=self.kwargs['worker_id'])
        context={'worker': worker}
        context['address'] = worker.Address
        latlang1 = getCoords(context['address'])
        print(latlang1)
        Company_list = Company.objects.all()
        d=100000
        Cid=-1
        for Comp in Company_list:
            if Comp.Industry_type==worker.Industry and Comp.Skill_required==worker.Skill:
                context['address'] = Comp.Address
                latlang2 = getCoords(context['address'])
                print(latlang2)
                distance = getdistance(latlang1,latlang2)
                print(distance)
                if distance < d:
                    Cid=Comp.id
                    print(Cid)
                    d = distance
        if Cid==-1:
            context['success'] = False
        else:
            context['success'] = True
            company = Company.objects.get(id=Cid)
            context['company'] = company
        return render(request, 'workforce/jobsearch.html', context)