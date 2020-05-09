import asyncio
from japronto import Application
import aiomysql
import json
from aiomysql.cursors import DictCursor
import requests_cache
requests_cache.install_cache('web_app', backend='sqlite', expire_after=180)


async def index(request):
    return request.Response(text="Hello from front page")


async def event(request):
    try:
        data = request.json
        response_obj = {'status': 'success',
                        'message': str(data['id']) + ', '+str(data['label'])}
        async with mysql.acquire() as conn:
            async with conn.cursor() as cur:
                cmd = "INSERT INTO Events (PageId, Label) VALUES (%d, %s)" % (
                int(data['id']), "'" + data['label'] + "'")
                await cur.execute(cmd)
        return request.Response(text=json.dumps(response_obj))
    except Exception as e:
        response_obj = {'status': 'failed!!!', 'message': str(e)}
        return request.Response(text=json.dumps(response_obj))


async def get_mysql_pool(loop):
    pool = await aiomysql.create_pool(
        host="mysql",
        user="aiomysql",
        password="mypass",
        db="deep_hard",
        cursorclass=DictCursor,
        loop=loop,
        autocommit=True
    )
    return pool


loop = asyncio.get_event_loop()
mysql = loop.run_until_complete(get_mysql_pool(loop))

app = Application()
router = app.router
router.add_route('/', index)
router.add_route('/event', handler=event, method='POST')
app._loop = loop
app.run(host='0.0.0.0', port=8888, debug=True)





