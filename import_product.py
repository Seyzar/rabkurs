import csv
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoshop.settings')

import django

django.setup()

from ecomapp.models import Category, Product, Brand

from decimal import Decimal

# with open(r"e:\downloads\01.12.2019\Мобильные телефоны.csv", encoding='utf-8') as data:
#     product_data = csv.DictReader(data, delimiter=';', fieldnames=(
#         "Категория", "Подкатегория 2", "Подкатегория 3", "Подкатегория 4", "Артикул", "Артикул модификации",
#         "Имя товара",
#         "Категория (полный путь)", "Цена", "Цена старая", "Цена закупки", "Количество", "Описание", "Краткое описание",
#         "Производитель", "Вес", "Meta title", "Meta keywords", "Meta description", "Фото (через пробел)",
#         "Ссылки на фото (через пробел)", "Характеристики (HTML/Table)", "Опция:Цвет"))
#
#     for product in product_data:
#         # print(product["Цена"].replace(',', '.').replace(' ', ''))
#         # print(Decimal(product["Цена"].replace(',', '.').replace(' ', '')))
#
#         Product.objects.create(
#             brand=Brand.objects.get_or_create(name=product["Производитель"])[0],
#             category=Category.objects.get(name=product["Категория"]),
#             title=product["Имя товара"],
#             description=product["Описание"],
#             price=Decimal(product["Цена"].replace(',', '.').replace(' ', '')),
#         )

from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify

def my_slugify_function(content):
    return content.replace('_', '-').lower()


for product in Product.objects.all():
    print(product.id, product.title)
    # product.slug = AutoSlugField(populate_from=[str(product.id), str(product.title)], slugify_function=my_slugify_function, editable=True)
    # slug = AutoSlugField(populate_from=[str(product.id), str(product.title)])
    product.slug = slugify([product.id, product.title])
    product.save()
    # product.save()
    # print(product.id, product.slug.__str__())
