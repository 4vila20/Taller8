#!/bin/bash
# Función para guardar la hora actual en el archivo save_hour.txt
save_hour() {
    date +"%H:%M:%S" > save_hour.txt
}

# Bucle infinito que guarda la hora cada 5 segundos
while true; do
    save_hour
    sleep 5
done &

