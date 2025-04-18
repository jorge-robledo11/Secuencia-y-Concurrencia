import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


def fib(n: int) -> int:
    """Cálculo recursivo de Fibonacci (ineficiente a propósito)."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

async def run_secuencial(tasks: list[int]) -> list[int]:
    """Ejecuta fib() una a una, midiendo tiempo total."""
    start = time.perf_counter()
    results = []
    for n in tasks:
        results.append(fib(n))
    dur = time.perf_counter() - start
    print(f"→ Secuencial ({len(tasks)} tareas): {dur:.3f} s")
    return results

async def run_concurrente(tasks: list[int]) -> list[int]:
    """Ejecuta fib() en paralelo usando ProcessPoolExecutor."""
    start = time.perf_counter()
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        # Dispara todas las tareas al pool de procesos
        futures = [
            loop.run_in_executor(pool, fib, n)
            for n in tasks
        ]
        results = await asyncio.gather(*futures)
    dur = time.perf_counter() - start
    print(f"→ Concurrente ({len(tasks)} tareas): {dur:.3f} s")
    return results

async def main():
    # Parámetros: lista de valores de Fibonacci a calcular
    # Aquí usamos 36, que tarda unos cuantos centésimas de segundo cada uno
    tasks = [36] * 10

    print("\n=== EJECUCIÓN SECUENCIAL ===")
    seq = await run_secuencial(tasks)

    print("\n=== EJECUCIÓN CONCURRENTE ===")
    conc = await run_concurrente(tasks)

    # Comprobación rápida de resultados
    print("\nResultados secuencial:", seq)
    print("Resultados concurrente:", conc)

if __name__ == "__main__":
    asyncio.run(main())
