from django.shortcuts import render
from django.http import HttpResponse
from forms import SpellingForm
from certografia.functions import correctText
from functions import markWord
from django.utils.html import escape

def home(request):
    if request.method == 'POST': 
        form = SpellingForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            correctedText = correctText(text)
            for result in correctedText:
                if result[0] != result[1]:
                    mark = markWord(result[0], result[1])
                    text = text.replace(result[1], mark)

            return render(request, 'core/result.html', {
                'result': text
            })
        else:
            return HttpResponse("Invalid Form")

    form = SpellingForm()

    return render(request, 'core/home.html', {
        'form': form,
    })