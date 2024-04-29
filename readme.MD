# Proyecto 8: Alimentando el conocimiento de un LLM

## Fundamentos teóricos

Los sistemas expertos representan una de las primeras y más exitosas aplicaciones de la inteligencia artificial en la resolución de problemas específicos mediante la emulación del razonamiento humano. Estos sistemas se basan en una base de conocimiento detallada y un motor de inferencia que aplica lógicas de decisión a los datos disponibles para generar conclusiones. A lo largo de las décadas, los sistemas expertos han evolucionado, pero su esencia permanece en la capacidad de ofrecer soluciones basadas en el conocimiento acumulado y estructurado de manera explícita.

Por otro lado, los **knowledge graphs** o grafos de conocimiento ofrecen una representación estructurada y semántica de información donde entidades, conceptos y las interrelaciones entre ellos se modelan de manera que reflejan su significado real y sus conexiones. Esta estructura facilita la interpretación automática y el acceso a información relevante y detallada, permitiendo a los sistemas que los utilizan tener una comprensión más profunda y un contexto más rico sobre los datos que manejan. Podrían servir como base de conocimiento de un sistema experto.

La integración de modelos de lenguaje de gran escala (LLM) con grafos de conocimiento presenta una oportunidad para superar algunas de las limitaciones que estos modelos enfrentan por sí solos, especialmente en términos de precisión y actualidad de la información que generan. Los LLMs, aunque excelentes en el procesamiento del lenguaje, a menudo carecen de acceso a información actualizada y verificada, lo que puede llevar a errores o "alucinaciones" en sus respuestas.

La combinación de un LLM con un grafo de conocimiento puede usarse como una solución prometedora. Aquí, el LLM puede beneficiarse de una base de conocimiento dinámica y estructurada que se actualiza continuamente, mejorando la relevancia y exactitud de las respuestas generadas. Además, esta integración permite al sistema experto no solo responder con datos precisos, sino también explicar el razonamiento detrás de sus conclusiones, aumentando la transparencia y la confianza en sus capacidades. De esta forma, estaríamos utilizando un LLM como motor de inferencia.

En este proyecto, exploraremos cómo la simbiosis entre los grafos de conocimiento y un LLM puede simular los procesos decisionales de un sistema experto, proporcionando un marco teórico y práctico para aplicaciones futuras en diversos campos, desde la medicina hasta el derecho, pasando por la asistencia personalizada y la educación.

### Objetivos del proyecto

- Desarrollar un sistema experto capaz de integrar y procesar información actualizada de manera autónoma utilizando knowledge graphs y un modelo de lenguaje grande (LLM).
- Evaluar la capacidad del sistema para adaptar sus estrategias de respuesta basándose en el análisis dinámico de los datos obtenidos a través del knowledge graph.

### Descripción del proyecto

1. Elegir un tema sobre el que quieras hacer un sistema experto.
2. Buscar una página con noticias o información sobre ese tema.
3. Hacer scrapping de la información de la página. Usa r.jina.ai para obtener la información en un formato más adecuado para un LLM.
4. Usa llamadas a un LLM para extraer los triplets relevantes de cada página.
5. Construye un sistema experto tal y como se describe en esta página.
6. Prueba a hacer alguna pregunta y a visualizar al menos una parte del grafo generado.

### Documentación del proyecto

Documenta todo el proceso en un archivo PDF, indicando:

- Los objetivos de tu sistema experto.
- Cuáles son los componentes de tu sistema experto.
- Los scripts utilizados.
- Una imagen con una representación visual parcial del grafo generado.
- Tu opinión acerca del uso de knowledge graphs y LLMs para modelar un sistema experto.
