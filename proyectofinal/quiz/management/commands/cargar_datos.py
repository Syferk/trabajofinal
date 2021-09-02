from django.core.management import BaseCommand
from quiz import models

from csv import DictReader


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open("./categorias.csv", 'r') as archivo:
            for fila in DictReader(archivo):
                cat = models.Category()
                cat.category_name = fila["categoria"]
                cat.question_number = fila["cantidad"]
                cat.save()

        with open("./preguntas.csv", 'r') as archivo:
            for fila in DictReader(archivo):
                preg = models.Question()
                preg.category = models.Category.objects.filter(category_name = fila["categoria"])[0]
                preg.question = fila["Pregunta"]
                preg.option1 = fila["Opcion1"]
                preg.option2 = fila["Opcion2"]
                preg.option3 = fila["Opcion3"]
                preg.option4 = fila["Opcion4"]
                preg.answer = fila["Respuesta"]
                category = preg.category
                category.question_available += 1
                category.save()
                preg.save()
