from datetime import date

from django.shortcuts import render

# Create your views here.

all_cafeterias = [
  {
    "slug": "ebais",
    "title": "Ebai's",
    "image": "ebais.jpeg",
    "description": "Ebai's Canteen",
    "availability": True,
    "date": date(2023, 6, 21),
  },
  {
    "slug": "gonzaga",
    "title": "Gonzaga",
    "image": "blueandgold.png",
    "description": "Gonzaga food cafeteria",
    "availability": True,
    "date": date(2023, 6, 10),
  },
  {
    "slug": "iggys",
    "title": "Iggys",
    "image": "iggys.png",
    "description": "Iggy's Food Hub.",
    "availability": True,
    "date": date(2023, 6, 22),
  },
  {
    "slug": "irh-kravers",
    "title": "IRH",
    "image": "kravers.png",
    "description": "Kraver's canteen in the IRH food hall.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
  {
    "slug": "jsec",
    "title": "JSEC",
    "image": "jsec.png",
    "description": "JGSOM Student Enterprise Center.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
]

def get_name(product):
  return product['title']

def starting_page(request):
  cafs_list = sorted(all_cafeterias, key=get_name)
  return render(request, "index.html", {
    "cafeterias": cafs_list
  })

def cafeterias(request):
  return render(request, "all_cafeterias.html", {
    "all_cafeterias": all_cafeterias
  })

def caf_detail(request, slug):
  specific_caf = next(product for product in all_cafeterias if product['slug'] == slug)
  return render(request, "caf_detail.html", {
    "cafeteria": specific_caf
  })