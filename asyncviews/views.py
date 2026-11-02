import asyncio
import httpx
from django.http import JsonResponse


def api_ficticia_view(request):
    return JsonResponse({
        'usuario': 'aluno_django',
        'status_da_aula': 'aprendendo_async',
        'plataforma': 'Uvicorn + HTTPX'
    })



async def contador_tempo_view(request):
    loop = asyncio.get_event_loop()
    inicio = loop.time()

    url_local = 'http://localhost:8000/api-ficticia/'

    async with httpx.AsyncClient() as client:
        try:
            resposta = await client.get(url_local)
            if resposta.status_code == 200:
                dados_da_api = resposta.json()
            else:
                dados_da_api = {'erro': f'Status inesperado: {resposta.status_code}'}
        except Exception as e:
            dados_da_api = {'erro': f'Falha ao conectar na API local: {str(e)}'}

    fim = loop.time()
    tempo_total = round(fim - inicio, 2)

    return JsonResponse({
        'status': 'Sucesso',
        'mensagem': 'Dados obtidos de forma assíncrona localmente!',
        'tempo_total': f'{tempo_total} segundos',
        'dados_recebidos': dados_da_api
    })



