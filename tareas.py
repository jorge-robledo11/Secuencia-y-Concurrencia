import asyncio

async def tarea(n):
    await asyncio.sleep(0.5)
    return n * 2

async def main():
    # Crear tasks para cada llamada
    tasks = [asyncio.create_task(tarea(i)) for i in range(10)]
    # Esperar a que todas terminen
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
