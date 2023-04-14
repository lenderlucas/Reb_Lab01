## What are the underlying mathematical principles behind UMAP? What is it useful for?

### UMAP: 
Es una técnica de reducción de dimensionalidad no lineal que utiliza principios matemáticos de grafos, geometría diferencial y topología algebraica para proyectar datos de alta dimensión en un espacio de menor dimensión, preservando las relaciones espaciales entre los datos

### Respecto a sus principios matematicos estos son:

* Teoría de grafos: 
En UMAP, la teoría de grafos se utiliza para construir un grafo de vecindades en el espacio de alta dimensión. Este grafo es un conjunto de nodos (datos) conectados por aristas, donde las aristas representan las relaciones de vecindad entre los datos. En términos matemáticos, un grafo se representa por medio de una tupla G = (V, E), donde V es el conjunto de vértices o nodos y E es el conjunto de aristas o conexiones entre los nodos. En UMAP, el grafo se construye utilizando una medida de distancia entre los datos y un umbral de distancia para determinar las conexiones entre los nodos.

* Geometría diferencial: 
En UMAP, la geometría diferencial se utiliza para medir las distancias entre los datos en el espacio de alta dimensión y en la proyección de baja dimensión. En particular, se utiliza una métrica no euclidiana llamada distancia de geodésica para medir las distancias en la proyección de baja dimensión. En términos matemáticos, la geometría diferencial estudia las propiedades geométricas de los objetos en el espacio que no cambian bajo transformaciones continuas. En UMAP, se utilizan técnicas de geometría diferencial para medir las distancias entre los datos y encontrar la proyección de baja dimensión que mejor preserva las relaciones de vecindad entre los datos.

* Topología algebraica: 
En UMAP, la topología algebraica se utiliza para analizar la estructura topológica del grafo de vecindades en el espacio de alta dimensión. En particular, se utiliza una técnica llamada persistencia homológica para identificar características topológicas importantes del grafo, como agujeros y cavidades. En términos matemáticos, la topología algebraica estudia las propiedades topológicas de los objetos utilizando herramientas de álgebra. En UMAP, se utilizan técnicas de topología algebraica para analizar la estructura topológica del grafo de vecindades y encontrar la proyección de baja dimensión que mejor preserva esta estructura.