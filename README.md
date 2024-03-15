# Proyecto de Predicción de Números de Lotería

Este es un proyecto destinado a predecir los números de la lotería utilizando técnicas de Machine Learning. El objetivo principal es desarrollar un modelo que pueda predecir los números ganadores en futuros sorteos de la lotería.

## Descripción

El proyecto utiliza un modelo de aprendizaje automático basado en árboles de decisión para predecir los números de la lotería. Se utilizan características como la suma de los números, el promedio, el mínimo, el máximo, el rango, la desviación estándar, la mediana, el día de la semana del sorteo, el mes del sorteo y el año del sorteo para entrenar el modelo.

## Estructura de archivos

- `balo1.py`: Script principal que carga los datos, entrena el modelo, realiza predicciones y muestra los resultados.
- `num.xlsx`: Archivo Excel que contiene los datos de entrada para el modelo.
- `README.md`: Este archivo que proporciona una descripción general del proyecto.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas necesarias instaladas. Puedes instalar las dependencias ejecutando `pip install -r requirements.txt`.

## Uso

1. Ejecuta el script `balo1.py` para entrenar el modelo y realizar predicciones.
2. El script mostrará las predicciones en el conjunto de prueba y también realizará una predicción para el próximo sorteo de lotería.

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor, abre un pull request explicando los cambios propuestos.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## ⚠️ Aviso Importante

**Las predicciones generadas por este proyecto se basan en un modelo de aprendizaje automático entrenado con datos históricos de sorteos de lotería. Es importante tener en cuenta que estas predicciones son resultado de una simulación y no aseguran el resultado real de futuros sorteos de la lotería. La lotería es un juego de azar y cada sorteo es independiente de los anteriores. Por lo tanto, se recomienda utilizar estas predicciones con precaución y no tomar decisiones financieras significativas basadas únicamente en ellas.**
