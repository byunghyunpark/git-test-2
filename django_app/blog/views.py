from django.shortcuts import render


def index(request):
    result = [i*2 for i in range(100000)]
    result2 = []
    for i, number in enumerate(result):
        result2.append((i, number))
    context = {
        "result": result2,
    }
    return render(request, 'index.html', context)
