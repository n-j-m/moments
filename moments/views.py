from django.views.generic.list import ListView

from moments.models import Moment


class MomentListView(ListView):
	model = Moment
	template_name = 'moments/moments.html'
