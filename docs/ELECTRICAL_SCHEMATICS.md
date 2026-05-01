# Esquemáticos Elétricos - Resumo

- Raspberry Pi 4: USB -> RTL-SDR, GPIO I2C -> MLX90640, UART -> GPS optional
- ESP32: UART (GPIO16/17) -> HLK-LD2410, I2C (21/22) -> MLX90640, GPIO13 -> PIR
- Power: 3x 18650 em paralelo -> UPS Booster 5V/3A -> Busbar (5V + GND)

Notas:
- Centralizar GND no busbar.
- Usar cabos I2C blindados se perto do SDR.
- Evitar linhas longas UART (>3m).
