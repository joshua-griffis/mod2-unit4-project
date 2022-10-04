from django.shortcuts import render
from django.http.response import HttpResponse
from dataclasses import dataclass
# Create your views here.


@dataclass
class Nen:
    description: str
    members: list
    image: str


def home(request):
    content = {"liszt": ["Enhancement", "Conjuration",
                         "Transmutation", "Emission", "Manipulation", "Specialist"]}
    return render(request, 'home.html', content)


def info(request, name):
    info = {
        "name": name,
        "nen": {
            "Enhancement": Nen(
                "Enhancement allows Enhancers to bolster and enhance the strength and quality of their Nen.",
                ["Gon Freecss", "Uvogin", "Wing", "Isaac Netero"],
                "images/enhancement.gif"
            ),
            "Transmutation": Nen(
                "Transmutation allows Transmuters to change the properties of their Nen so that it mimics proporties of something else like the elasticity of gum or the proporties of electricity.",
                ["Killua Zoldyck", "Hisoka Morow", "Feitan", "Silva Zoldyck"],
                "images/transmutation.gif"
            ),
            "Conjuration": Nen(
                "Conjuration allows Conjurers to materialize their Nen into physical objects like chains or weapons.",
                ["Kurapika", "kite", "Shizuku", "Kortopi"],
                "images/conjuration.gif"
            ),
            "Emission": Nen(
                "Emission allows Emitters to emit their Nen from there body and fire it outward at a ranged distance.",
                ["Leorio", "Razor", "Knuckle", "Franklin"],
                "images/emission.gif"
            ),
            "Manipulation": Nen(
                "Manipulation allows Manipulators to use their Nen to control the movement or action of a certain person, object, or other ability.",
                ["Illumi Zoldyck", "Morel", "Shalnark", "Pouf"],
                "images/manipulation.gif"
            ),
            "Specialist": Nen(
                "Specialization is for anything that doesn’t fit squarely into any of the other five categories. Specialists usually have abilities that cannot be gained through training and they often have effects that cannot be replicated.",
                ["Chrollo Lucifer", "Meruem", "Pitou", "Emperor Time Kurapika"],
                "images/specialist.gif"
            ),
        }
    }
    return render(request, 'info.html', info)
