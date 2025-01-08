mascotas = ["perro", "gato", "conejo", "tortuga", "hamster"]

for mascota in enumerate(mascotas):
    print(mascota)
    # output:
    # (0, 'perro'),
    # (1, 'gato'),
    # (2, 'conejo'),
    # (3, 'tortuga'),
    # (4, 'hamster')

for i, mascota in enumerate(mascotas):
    print(f"Índice: {i}, Mascota: {mascota}")
    # output:
    # Índice: 0, Mascota: perro
    # Índice: 1, Mascota: gato
    # Índice: 2, Mascota: conejo
    # Índice: 3, Mascota: tortuga
    # Índice: 4, Mascota: hamster
