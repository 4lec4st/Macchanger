# Macchanger

Este script permite cambiar la dirección MAC de una interfaz de red en sistemas basados en Unix utilizando el comando `ifconfig`. Puede ser útil para pruebas de seguridad, privacidad o pruebas de red.

## Requisitos
- Python 3.x
- Permisos de superusuario (root)
- ifconfig instalado (normalmente disponible en sistemas Unix)

## Instalación
1. Clona el repositorio o guarda el script en tu máquina.
2. Asegúrate de que el script tenga permisos de ejecución:
```bash
chmod +x macchanger.py
```

## Uso
Ejecuta el script con permisos de superusuario:
```bash
sudo ./macchanger.py -i <interfaz> -m <nueva_MAC>
```

### Ejemplo
```bash
sudo ./macchanger.py -i eth0 -m 00:11:22:33:44:55
```

### Salida Esperada
- Si la entrada es válida, la dirección MAC cambia sin mensaje de confirmación.
- Si la entrada es inválida, se muestra:
```
[-] Invalid input
```
- Si se presiona Ctrl+C durante la ejecución, se muestra:
```
[!] Saliendo...
```
## Nota
Este script solo funciona en sistemas Unix y requiere permisos de root.


