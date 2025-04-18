# Proyecto de Corutinas Python

Este proyecto es una demostración práctica de programación asíncrona en Python, diseñado para ilustrar diferentes patrones y técnicas de concurrencia y paralelismo utilizando `asyncio` y `ProcessPoolExecutor`.

## 🎯 Introducción

### Objetivo del Proyecto
El objetivo principal es mostrar cómo implementar y utilizar diferentes patrones de programación asíncrona en Python, proporcionando ejemplos prácticos que demuestran las ventajas y casos de uso de cada enfoque.

### Contexto y Relevancia
La programación asíncrona es fundamental en el desarrollo de aplicaciones modernas por varias razones:
- Mejora significativa del rendimiento en operaciones I/O-bound
- Optimización del uso de recursos del sistema
- Capacidad para manejar múltiples tareas concurrentemente
- Escalabilidad mejorada en aplicaciones con alta carga de trabajo

## 🗂️ Estructura del Proyecto

### Archivos Principales
- `corutinas.py`: Ejemplo básico que introduce el concepto de corrutinas y la sintaxis async/await
- `tareas.py`: Demuestra la creación y gestión de Tasks usando asyncio
- `comparar_tasks.py`: Compara la ejecución secuencial vs concurrente en operaciones I/O-bound
- `comparar_procesos.py`: Ilustra el uso de ProcessPoolExecutor para operaciones CPU-bound

### Dependencias
- Python 3.x
- asyncio (incluido en la biblioteca estándar de Python)
- No requiere instalación de paquetes adicionales

## 💡 Conceptos Demostrados

### Corutinas Básicas
```python
async def hola():
    print("Antes de await")
    await asyncio.sleep(1)
    print("Después de await")
    return "¡Listo!"
```
Este ejemplo básico muestra:
- Sintaxis async/await
- Funcionamiento del event loop
- Suspensión y reanudación de funciones

### Tasks en asyncio
```python
async def run_concurrente(n: int):
    tasks = [asyncio.create_task(tarea(i)) for i in range(n)]
    resultados = await asyncio.gather(*tasks)
```
Características demostradas:
- Creación de múltiples tareas
- Ejecución concurrente
- Recolección de resultados con gather

### Concurrencia vs Paralelismo
El proyecto demuestra las diferencias entre:
- **Concurrencia**: Manejo de múltiples tareas I/O-bound usando asyncio
- **Paralelismo**: Procesamiento de tareas CPU-bound usando ProcessPoolExecutor

## 🚀 Ejemplos y Casos de Uso

### I/O-bound Tasks
Ejemplo de `comparar_tasks.py`:
```python
async def tarea(i: int) -> int:
    await asyncio.sleep(0.5)  # Simula operación I/O
    return i * 2
```
Este caso demuestra:
- Simulación de operaciones I/O usando sleep
- Comparación de rendimiento entre ejecución secuencial y concurrente
- Beneficios de la concurrencia en operaciones I/O-bound

### CPU-bound Tasks
Ejemplo de `comparar_procesos.py`:
```python
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```
Este caso ilustra:
- Cálculo recursivo de Fibonacci como tarea CPU-intensiva
- Uso de ProcessPoolExecutor para paralelismo real
- Comparación de rendimiento entre ejecución secuencial y paralela

## 📊 Resultados y Comparativas

### Comparativas de Rendimiento

#### I/O-bound Tasks (10 tareas)
- **Ejecución Secuencial**: ~5 segundos (0.5s × 10)
- **Ejecución Concurrente**: ~0.5 segundos (todas las tareas en paralelo)

#### CPU-bound Tasks (Fibonacci)
- **Ejecución Secuencial**: Tiempo proporcional a n × número de tareas
- **Ejecución Paralela**: Mejora significativa en sistemas multicore

### Análisis de Resultados

#### Cuándo usar cada enfoque:

1. **Concurrencia con asyncio**:
   - Operaciones I/O-bound (red, archivos, etc.)
   - Muchas tareas independientes
   - Necesidad de mantener alta concurrencia

2. **Paralelismo con ProcessPoolExecutor**:
   - Operaciones CPU-bound
   - Cálculos intensivos
   - Aprovechamiento de múltiples núcleos

## 📝 Conclusiones

Este proyecto demuestra que:
1. La programación asíncrona es esencial para aplicaciones modernas eficientes
2. Python proporciona herramientas poderosas para manejar tanto concurrencia como paralelismo
3. La elección entre concurrencia y paralelismo depende del tipo de tarea a realizar

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Algunos aspectos que podrían mejorarse:
- Agregar más ejemplos prácticos
- Implementar casos de uso reales
- Mejorar la documentación
- Agregar pruebas unitarias
