#!/usr/bin/env python3
import psutil

# Obtener memoria usada en MB
ram_usada = psutil.virtual_memory().used / (1024 * 1024)
print(f"{ram_usada:.2f}")
