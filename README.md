# Sprint 0 - Integración a un proyecto existente

## Propósito

Este repositorio representa un proyecto heredado. La consulta general `GET /libros` ya funciona. El equipo debe comprender el flujo completo y completar los endpoints restantes sin memorizar código.

## Arquitectura

`cliente.py -> HTTP -> app.py -> database.py -> Supabase`

## Preparación

```bash
git clone <URL_DEL_REPOSITORIO>
cd dai-sprint-0
python -m venv .venv
```

Activación en Windows:

```bash
.venv\Scripts\activate
```

Instalación y configuración:

```bash
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Complete `.env` con la URL y la clave publicable del proyecto Supabase.

## Estado inicial

| Método | Ruta | Estado |
|---|---|---|
| GET | `/` | Completo |
| GET | `/libros` | Completo |
| GET | `/libros/<id>` | Pendiente |
| POST | `/libros` | Pendiente |
| PUT | `/libros/<id>` | Pendiente |
| DELETE | `/libros/<id>` | Pendiente |

## Flujo de trabajo

1. Ejecute y pruebe lo existente.
2. Lea `app.py` y `database.py` antes de editar.
3. Complete un endpoint a la vez.
4. Después de cada cambio, pruebe en Postman.
5. Haga commits pequeños y descriptivos.

Ejemplos:

```bash
git commit -m "Implementa consulta de libro por id"
git commit -m "Implementa creación de libros"
git commit -m "Completa actualización y eliminación"
```

## Criterio central

No se evalúa recordar la sintaxis exacta. Se evalúa comprender dónde pertenece cada responsabilidad, consultar documentación y conectar correctamente las piezas.
