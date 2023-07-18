from datetime import date
from django.shortcuts import render
from .models import Tables

# Create your views here.

all_cafs = [
  {
    "slug": "ebais",
    "title": "Ebai's",
    "image": "ebais.jpeg",
    "menu": "jolly1.png",
    "tables": "irh_tables.png",
    "description": "Ebai's Canteen",
    "availability": True,
    "date": date(2023, 6, 21),
  },
  {
    "slug": "gonzaga",
    "title": "Gonzaga",
    "image": "blueandgold.png",
    "menu": "jolly2.jpeg",
    "tables": "irh_tables.png",
    "description": "Gonzaga food cafeteria",
    "availability": True,
    "date": date(2023, 6, 10),
  },
  {
    "slug": "iggys",
    "title": "Iggys",
    "image": "iggys.png",
    "menu": "jolly1.png",
    "tables": "irh_tables.png",
    "description": "Iggy's Food Hub.",
    "availability": True,
    "date": date(2023, 6, 22),
  },
  {
    "slug": "irh-kravers",
    "title": "IRH",
    "image": "kravers.png",
    "menu": "jolly2.jpeg",
    "tables": "irh_tables.png",
    "price": 500,
    "description": "Kraver's canteen in the IRH food hall.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
  {
    "slug": "jsec",
    "title": "JSEC",
    "image": "jsec.png",
    "menu": "jolly1.png",
    "tables": "irh_tables.png",
    "description": "JGSOM Student Enterprise Center.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
]

def get_name(caf):
  return caf['title']

def starting_page(request):
  sorted_products = sorted(all_cafs, key=get_name)
  return render(request, "store/index.html", {
    "cafs": sorted_products
  })

def cafs(request):
  return render(request, "store/all_cafs.html", {
    "all_cafs": all_cafs
  })

def caf_detail(request, slug):
  identified_caf = next(caf for caf in all_cafs if caf['slug'] == slug)
  return render(request, "store/caf_detail.html", {
    "caf": identified_caf
  })

def table_detail(request, slug):
  identified_caf = next(caf for caf in all_cafs if caf['slug'] == slug)
  return render(request, "store/tables.html", {
    "caf": identified_caf
  })

def tables(request):
	tables = Tables.objects.all()
	return render(request, "store/tables.html", {
      'tables':tables
  })