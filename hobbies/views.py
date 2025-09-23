from django.shortcuts import render
from django.http import Http404

hobbies = [
    {
        'id': 1,
        'name': 'Bambu Lab P1S 3D Printing',
        'slug': 'bambu-lab-p1s-3d-printing',
        'description': 'Exploring high-speed, multi-color 3D printing with the Bambu Lab P1S.',
        'image': 'portfolio/images/bambu_lab_p1s.jpg',
    },
    {
        'id': 2,
        'name': 'Lorcana',
        'slug': 'lorcana',
        'description': 'Collecting and playing the Disney Lorcana trading card game.',
        'image': 'portfolio/images/lorcana.jpg',
    },
]

def hobby_list(request):
    return render(request, 'hobbies/hobby_list.html', {'hobbies': hobbies})

def hobby_detail(request, slug):
    for hobby in hobbies:
        if hobby['slug'] == slug:
            return render(request, 'hobbies/hobby_detail.html', {'hobby': hobby})
    raise Http404("Hobby not found")
