from django.shortcuts import render
from django.http import Http404

projects = [
    {
        'id': 1,
        'title': 'Wonderful Quotes',
        'slug': 'wonderful-quotes',
        'summary': 'A responsive quote site that allows users to save and view inspirational quotes with animations and routing.',
        'technologies': ['React', 'React Router', 'Framer Motion'],
        'image': 'portfolio/images/quote.png',
    },
    {
        'id': 2,
        'title': 'Recipe App',
        'slug': 'recipe-app',
        'summary': 'A Firebase-powered recipe manager that lets users view, add, and store recipes with ingredients and instructions.',
        'technologies': ['React', 'Firebase', 'CSS'],
        'image': 'portfolio/images/recipe.png',
    },
    {
        'id': 3,
        'title': 'Food Ordering App',
        'slug': 'food-ordering-app',
        'summary': 'A meals store with cart functionality, allowing users to browse and simulate ordering meals with a modern UI.',
        'technologies': ['React', 'CSS', 'React Context API'],
        'image': 'portfolio/images/store.png',
    },
    {
        'id': 4,
        'title': 'My Hobbies',
        'slug': 'my-hobbies',
        'summary': 'A responsive React app for hobby tracking, enabling users to add and manage hobbies.',
        'technologies': ['React', 'CSS', 'React Context API'],
        'image': 'portfolio/images/hobby.jpg',
    },
    {
        'id': 5,
        'title': 'LP Lorcana',
        'slug': 'lp-lorcana',
        'summary': 'A landing page for Lorcana fans with sleek design and smooth navigation, showcasing a vibrant card game community.',
        'technologies': ['React', 'CSS', 'React Context API'],
        'image': 'portfolio/images/lp_lorcana.jpg',
    },
    {
        'id': 6,
        'title': 'Weather API',
        'slug': 'weather-api',
        'summary': 'A real-time weather forecast app with a clean, card-based UI and searchable locations.',
        'technologies': ['React', 'CSS', 'React Context API'],
        'image': 'portfolio/images/weather_api.jpg',
    },
]

def home(request):
    featured_projects = projects[:3]
    return render(request, 'home.html', {
        'projects': featured_projects,
        'project_detail_url_name': 'portfolio:project_detail', 
    })

def project_list(request):
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, slug):
    for project in projects:
        if project['slug'] == slug:
            return render(request, 'projects/project_detail.html', {'project': project})
    raise Http404("Project not found")
