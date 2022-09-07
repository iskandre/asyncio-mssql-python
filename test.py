import aioodbc
import pytest
import asyncio
loop = asyncio.get_event_loop()

CONN_STRING = (
        "DRIVER=ODBC Driver 17 for SQL Server;"
        F"SERVER={SERVER};"
        F"DATABASE={DB};"
        F"UID={DB_USER};PWD={DB_PASSWORD};"
    )

@pytest.mark.asyncio
async def test_default_loop(loop, dsn):
    asyncio.set_event_loop(loop)
    conn = await aioodbc.connect(dsn=dsn)
    print('connected')
    assert conn._loop is loop
    await conn.close()

coro = test_default_loop(loop, CONN_STRING)
loop.run_until_complete(coro)