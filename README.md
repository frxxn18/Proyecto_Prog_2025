# Proyecto de Gestión de Préstamos de Libros 📚

Este proyecto en Python permite la gestión completa de préstamos de libros en un centro educativo, utilizando una interfaz de consola estructurada por menús. Toda la información se almacena en archivos `.json`, y se apoya en la librería `pandas` para manipulación de datos y `os` para la navegación por menús.

---

## Tecnologías utilizadas

- Python 3.10+
- `pandas`
- `json`
- `os`
- `unittest` (para pruebas)
- phpMyAdmin (solo como contexto de base de datos, pero aquí usamos JSON)

---

## Estructura del Proyecto

```
Proyecto_Prog_2025/
├── app.py                     # Archivo principal
├── data/                      # Archivos JSON de alumnos, libros, cursos, etc.
├── models/                   # Clases: Alumno, Libro, Prestamo, Curso, Materia
├── utils/                    # Funciones auxiliares: validadores, exportadores, DataManager
├── menus/                    # Menús de navegación
├── tests/                    # Pruebas unitarias organizadas por módulo
├── test_generador.py         # Script para generar datos de prueba
├── main_tests.py             # Ejecuta todos los tests de forma agrupada
└── README.md
```

---

## ¿Qué puedes hacer con esta aplicación?

- Cargar y gestionar alumnos, libros, cursos y materias
- Registrar, devolver y cerrar préstamos
- Generar contratos de préstamo en TXT
- Exportar y vaciar datos
- Listar información por NIE, curso, estado o materia
- Probar todas las funcionalidades con tests automáticos

---

## Pruebas automáticas

Lanzar todos los tests:

```bash
python main_tests.py
```

Todos los tests deben pasar con:

```
Ran 30 tests in XXs
OK
```

---

##  ¿Cómo se ejecuta?

```bash
python app.py
```

Puedes navegar con las teclas por los menús y acceder a todas las opciones del sistema.

---

##  Datos iniciales incluidos

Se incluyen archivos `.json` en `/data` con información ya cargada para que puedas probar la aplicación directamente sin tener que añadir datos manualmente.

---

##  Proyecto desarrollado por:

- **Francisco Pardo Doñoro**
- Curso 2024/2025 — IES Arcipreste de Hita

---

## Notas finales

- Codificación UTF-8 usada para soportar acentos y eñes
- Asegurado el uso de `ensure_ascii=False` en todos los `json.dump` para que se vean legibles los JSON
- Tests implementados con `unittest` para cada funcionalidad
- Nada que no se haya dado en clase antes o esté fuera de la documentacion dada
