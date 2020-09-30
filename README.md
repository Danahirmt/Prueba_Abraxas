# Forecast Demand
Prueba técnica de Grupo Abraxas
## Objetivo

Pronosticar la demanda de un producto para una semana determinada, a una tienda particular. El conjunto de datos que se proporciona consta de 8 semanas de transacciones de ventas en México.
Cada semana, hay camiones de reparto que entregan productos a los proveedores. La transacción consiste en ventas y devoluciones. Las devoluciones son los productos que no se venden y caducan. La demanda de un producto en una semana determinada se define como las ventas de esta semana restado por el retorno la semana que viene.

#### Descripción de archivos
+ cliente_tabla.csv — client names (can be joined with train/test on Cliente_ID)
+ producto_tabla.csv — product names (can be joined with train/test on
Producto_ID)
+ town_state.csv — town and state (can be joined with train/test on Agencia_ID)


#### Descripción de atributos

+ Semana — Week number (From Thursday to Wednesday)
+ Agencia_ID — Sales Depot ID
+ Canal_ID — Sales Channel ID
+ Ruta_SAK — Route ID (Several routes = Sales Depot)
+ Cliente_ID — Client ID
+ NombreCliente — Client name
+ Producto_ID — Product ID
+ NombreProducto — Product Name
+ Venta_uni_hoy — Sales unit this week (integer)
+ Venta_hoy — Sales this week (unit: pesos)
+ Dev_uni_proxima — Returns unit next week (integer)
+ Dev_proxima — Returns next week (unit: pesos)
+ Demanda_uni_equil — Adjusted Demand (integer) (This is the target you will
predict)


#### Organización de repositorio
````
├── README.md
├── carga_datos.py <- cargar los archivos
├── data <- archivos porporcionados
│   ├── cliente_tabla.csv
│   ├── df_[candidate]_small.csv
│   ├── df_[test]_small.csv
│   ├── producto_tabla.csv
│   └── town_state_small.csv
├── notebook.ipynb <- Desarrollo de proyecto y resultados
└── utils.py <- funciones necesarias para el desarrollo
````
 #### Workflow
 + Lectura de datos
 + Estandarización
 + Series de tiempo
    + La selección de cliente, agencia y producto fue por medio de frecuencias, se seleccionaron los dos productos con mayor frecuencia y sus respectivas principales agencias y clientes. Se realizan dos series de tiempo de ambos productos por las 8 semanas proporcionadas en el conjunto train
 + Muestra de clientes que representa una agencia
    + La agencia seleccionada fue la 1123 por su gran participación en el mercado
    + La selección de clientes se baso en el orden de mayor a menor de sus frecuencias, por otro lado el número de muestra fue de 13 clientes de 3299, seleccionado aquello que representaban poco más del 7% de los datos a pesas de ser menos del 0.03% de estos, siendo los que más influyen en la agencia.
 + Productos top 3 de la muestra de clientes obtenidos por frecuencia (nito, mantecadas y rebanadas)
 + Predicciones usando XGboost un modelo de machine learning el cual destaca en sus aplicaciones en temas relacionado dado su gran desempeño, la función de pérdida utilizada fue RSML.
 + Concatenación de dataframe con predicciones de la semana 9 para poder realizar gráficas de series de tiempo. Fue presentada para el Cliente Lupita 
 
 Siguientes pasos: Ajustar los pármetros del modelo para obtener un mejor desempeño
 
