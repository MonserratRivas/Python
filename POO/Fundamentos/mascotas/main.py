from ninja import Ninja
from mascotas import Mascota

kitty = Mascota('kitty','gato','churu')
alexandra = Ninja('alexandra','-',100,100, 'kitty')

kitty.comer()
kitty.dormir()
kitty.MostrarEnergia()
kitty.MostrarSalud()