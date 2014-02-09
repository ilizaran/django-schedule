from django import forms
from django.utils.translation import ugettext_lazy as _
<<<<<<< HEAD
from schedule.models import Event, Occurrence, Rule
=======
from schedule.models import Event, Occurrence
>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
import datetime
import time


class SpanForm(forms.ModelForm):

    start = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    end = forms.DateTimeField(widget=forms.SplitDateTimeWidget, help_text = _("The end time must be later than start time."))

    def clean_end(self):
        if self.cleaned_data['end'] <= self.cleaned_data['start']:
            raise forms.ValidationError(_("The end time must be later than start time."))
        return self.cleaned_data['end']


class EventForm(SpanForm):
    def __init__(self, hour24=False, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
    
    end_recurring_period = forms.DateTimeField(help_text = _("This date is ignored for one time only events."), required=False)
    
    class Meta:
        model = Event
        exclude = ('creator', 'created_on', 'calendar')
        

class OccurrenceForm(SpanForm):
    
    class Meta:
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled')


<<<<<<< HEAD
class OccurrenceBackendForm(SpanForm):
    """
        used only for processing data (for ajax methods)
    """

    start = forms.DateTimeField()
    end = forms.DateTimeField()

    class Meta:
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled')


class EventBackendForm(SpanForm):

    start = forms.DateTimeField()
    end = forms.DateTimeField()
    end_recurring_period = forms.DateTimeField(required=False)

    class Meta:
        model = Event
        exclude = ('creator', 'created_on', 'calendar')


=======
>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
class RuleForm(forms.ModelForm):
    params = forms.CharField(widget=forms.Textarea, help_text=_("Extra parameters to define this type of recursion. Should follow this format: rruleparam:value;otherparam:value."))

    def clean_params(self):
        params = self.cleaned_data["params"]
        try:
<<<<<<< HEAD
            Rule(params=params).get_params()
        except (ValueError, SyntaxError):
            raise forms.ValidationError(_("Params format looks invalid"))
        return self.cleaned_data["params"]


=======
            params = params.split(';')
            for param in params:
                param = param.split(':')
                if len(param) == 2:
                    param = (str(param[0]), [int(p) for p in param[1].split(',')])
                    if len(param[1]) == 1:
                        param = (param[0], param[1][0])
        except ValueError:
            raise forms.ValidationError(_("Params format looks invalide"))
        return self.cleaned_data["params"]
>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
