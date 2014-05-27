from django.forms import ModelForm
from core.models import *

class PolygonForm(ModelForm):
	class Meta:
		model = Polygon


class QuarryForm(ModelForm):
	class Meta:
		model = Price

	def __init__(self, *args, **kwargs):
		super(QuarryForm, self).__init__(*args, **kwargs)
		self.fields['quarry'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tri_axel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tractor_trailer'].widget.attrs.update({'class' : 'form-control'})
		self.fields['stone_slinger'].widget.attrs.update({'class' : 'form-control'})