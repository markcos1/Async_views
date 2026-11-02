import asyncio
import time
from django.http import JsonResponse


# Create your views here.
async def contador_tempo_view(request):
    inicio = time.time()

    await asyncio.sleep(5)

    fim = time.time()
    tempo_total = round(fim - inicio, 2)

    return JsonResponse({
        'status': 'Sucesso',
        'mensagem': 'Contagem finalizada',
        'tempo_total': f'{tempo_total} segundos'
    })

