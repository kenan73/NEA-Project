from pygame.image import load 
from pygame.math import Vector2

def load_image(name, with_alpha=True):
    path = f'assets/sprites/{name}.png'
    print(f"Loading sprite from: {path}")
    loaded_sprite = load(path)
    
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def load_sprite(name, with_alpha=True):
    path = f'assets/sprites/{name}.png'
    loaded_sprite = load(path)
    
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def wrap_object(position, surface):
    x, y = position
    

    
       