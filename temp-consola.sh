#!/bin/bash
# Script: temp-consola.sh
# Proposito: Mostrar temperatura de CPU y GPU del Raspberry
# Editado por Raspbo
# Ejecucion: ./temp-consola.sh
# -------------------------------------------------------
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"

