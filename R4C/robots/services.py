import io
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Robot
from openpyxl import Workbook


def create_data_to_excel():
    """
    Функция создает отчет в формате Excel по моделям роботов.
    """
    # Получаем текущее время
    time_now = timezone.now()
    # Получаем время неделю назад
    time_one_week_ago = timezone.now() - timedelta(days=7)

    # Инициализируем объекты Workbook и BytesIO
    output = io.BytesIO()
    wb = Workbook()

    # Получаем список моделей роботов
    models_list = Robot.objects.values_list('model', flat=True).distinct()
    # Генермруем страницу с зоголовками м записями
    for model in models_list:
        ws = wb.create_sheet(model)
        ws.append(['Модель', 'Версия', 'Количество за неделю'])
        queryset = Robot.objects.filter(model=model, created__gte=time_one_week_ago, created__lte=time_now).values(
            'version').annotate(
            total=Count('version'))
        # Записываем полученную информацию в файл Excel
        for item in queryset:
            ws.append([model, item['version'], item['total']])
    # Сохраняем файл и возвращаем
    wb.save(output)
    output.seek(0)
    return output
