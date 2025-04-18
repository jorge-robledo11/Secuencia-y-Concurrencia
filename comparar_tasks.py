import asyncio
import time

async def tarea(i: int) -> int:
    """Simula una operación I/O-bound de 0.5 segundos y devuelve i*2."""
    await asyncio.sleep(0.5)
    return i * 2

async def run_secuencial(n: int) -> list[int]:
    """Ejecuta `tarea` una a una, esperando cada resultado."""
    start = time.perf_counter()
    resultados = []
    for i in range(n):
        resultados.append(await tarea(i))
    dur = time.perf_counter() - start
    print(f"Secuencial ({n} tareas): {dur:.3f} s")
    return resultados

async def run_concurrente(n: int) -> list[int]:
    """Ejecuta `tarea` en paralelo creando Tasks y luego esperando todos."""
    start = time.perf_counter()
    tasks = [asyncio.create_task(tarea(i)) for i in range(n)]
    resultados = await asyncio.gather(*tasks)
    dur = time.perf_counter() - start
    print(f"Concurrente ({n} tareas): {dur:.3f} s")
    return resultados

async def main():
    n = 10
    print("\n>>> EJECUCIÓN SECUENCIAL:")
    seq = await run_secuencial(n)

    print("\n>>> EJECUCIÓN CONCURRENTE:")
    conc = await run_concurrente(n)

    print("\nResultados (secuencial):", seq)
    print("Resultados (concurrente):", conc)

if __name__ == "__main__":
    asyncio.run(main())
