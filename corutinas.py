import asyncio

async def hola():
    print("Antes de await")
    # Simula una operación I/O que dura 1 s
    await asyncio.sleep(1)
    print("Después de await")
    return "¡Listo!"

# Ejecutar la coroutine desde el event loop
result = asyncio.run(hola())
print(result)  # → "¡Listo!"