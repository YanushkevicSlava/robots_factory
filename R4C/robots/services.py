import io
from django.db.models import Count
from .models import Robot
from openpyxl import Workbook
from datetime import timedelta
from django.utils import timezone


def create_data_to_excel():
    """
    Функция создает отчет в формате Excel по моделям роботов.
    """

    # Получаем время неделю назад
    time_week_ago = timezone.now() - timedelta(days=7)

    # Инициализируем объекты Workbook и BytesIO
    output = io.BytesIO()
    wb = Workbook()

    # Получаем список моделей роботов
    models_list = Robot.objects.values_list('model', flat=True).distinct()
    # Генерируем страницу с зоголовками и записями
    for model in models_list:
        ws = wb.create_sheet(model)
        ws.append(['Модель', 'Версия', 'Количество за неделю'])
        queryset = Robot.objects.filter(model=model, created__gt=time_week_ago).values(
            'version').annotate(
            total=Count('version'))
        # Записываем полученную информацию в файл Excel
        for item in queryset:
            ws.append([model, item['version'], item['total']])
    # Сохраняем файл и возвращаем
    wb.save(output)
    output.seek(0)
    return output
