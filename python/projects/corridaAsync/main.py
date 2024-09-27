import asyncio

async def flash_correr():
    print('O flash começou a correr')

    await asyncio.sleep(3)
    print('O flash chegou!!')

async def superman_correr():
    print('Superman começou a correr')

    await asyncio.sleep(5)
    print('superman Chegou!!')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.gather(superman_correr(), flash_correr()))