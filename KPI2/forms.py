from django import forms

from commsquare.models import Interval


class GetKPI2ValidationForm(forms.Form):
    cell_id = forms.UUIDField(required=False)
    number_of_unique_users = forms.IntegerField(required=False)
    interval_start_timestamp_ge = forms.DateTimeField(required=False)
    interval_start_timestamp_le = forms.DateTimeField(required=False)
    interval_end_timestamp_ge = forms.DateTimeField(required=False)
    interval_end_timestamp_le = forms.DateTimeField(required=False)
    interval = forms.ChoiceField(
        choices=Interval.choices,
        required=False,
    )

    def is_valid(self):
        if not self.is_bound or self.errors:
            return False
        if not (
                not self.cleaned_data['interval_start_timestamp_le']
                or not self.cleaned_data['interval_start_timestamp_ge']
                or self.cleaned_data['interval_start_timestamp_le']
                >= self.cleaned_data['interval_start_timestamp_ge']
        ):
            self.errors['interval_start_timestamp_le, interval_start_timestamp_ge'] = (
                'Query param interval_start_timestamp_le should be greater than or equal to interval_start_timestamp_ge'
            )
            return False
        if not (
                not self.cleaned_data['interval_end_timestamp_le']
                or not self.cleaned_data['interval_end_timestamp_ge']
                or self.cleaned_data['interval_end_timestamp_le']
                >= self.cleaned_data['interval_end_timestamp_ge']
        ):
            self.errors['interval_end_timestamp_le, interval_end_timestamp_ge'] = (
                'Query param interval_end_timestamp_le should be greater than or equal to interval_end_timestamp_ge'
            )
            return False
        return True
