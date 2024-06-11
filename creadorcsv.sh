#!/bin/bash

# Encabezado del archivo CSV
echo "Fecha,Hora,Memoria total (kB),Memoria usada (kB),Memoria libre (kB),Memoria compartida (kB),Buffer (kB),Caché (kB),Memoria disponible (kB)" > recursos.csv

# Función para obtener las estadísticas de memoria y guardarlas en el archivo CSV
save_memory_stats() {
    # Obtener la fecha y hora actual
    fecha=$(date +"%Y-%m-%d")
    hora=$(date +"%H:%M:%S")

    # Obtener estadísticas de memoria usando el comando 'free'
    memoria_stats=$(free -k | grep Mem | awk '{print $2","$3","$4","$5","$6","$7","$8}')

    # Guardar las estadísticas en el archivo CSV
    echo "$fecha,$hora,$memoria_stats" >> recursos.csv
}

# Bucle infinito que guarda las estadísticas cada 5 segundos
while true; do
    save_memory_stats
    sleep 5
done &



