from django.shortcuts import render
from django import forms
import decimal

# Enable use of decimals up to 2 points
decimal.getcontext().prec = 2

# Get_samples function
def get_results(data, samples):

    best_fits = []
    previous_value = data[0]
    data.sort()

    # Find the best fit for each sample
    for sample in samples:
        for value in data:
            # If value equals sample, use this value and remove it from data
            if value == sample:
                best_fits.append(value)
                data.remove(value)
                break
            # If value is smaller than sample, save and move on to next value
            elif value < sample:
                previous_value = value
            # If value is larger than sample, use value closest to the sample
            elif value > sample:
                over = value - sample
                under = sample - previous_value
                if under <= over:
                    best_fits.append(previous_value)
                    data.remove(previous_value)
                    break
                elif over < under:
                    best_fits.append(value)
                    data.remove(value)
                    break
        
    return best_fits

class SampleForm(forms.Form):
    excel_data = forms.CharField(label="Data From Excel")
    excel_samples = forms.CharField(label="Samples From Excel")


def index(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            # Convert form data and samples into a list
            excel_data = form.cleaned_data["excel_data"]
            excel_data_list = excel_data.split(' ')
            excel_samples = form.cleaned_data["excel_samples"]
            excel_samples_list = excel_samples.split(' ')

            # Convert strings in lists to integeres
            excel_data_list = [decimal.Decimal(x) for x in excel_data_list]
            excel_samples_list = [decimal.Decimal(x) for x in excel_samples_list]

            # Generate Results
            results_in_list = get_results(excel_data_list, excel_samples_list)

            # Convert results_in_list to excel-friendly strings of data
            results_in_list = [str(x) for x in results_in_list]
            results_for_export = '\n'.join(results_in_list)

            return render(request, "sampling/index.html", {
                "form": SampleForm(),
                "results": results_for_export
            })
    else:
        return render(request, "sampling/index.html", {
            "form": SampleForm(),
            "results": ""
        })

