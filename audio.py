from pygame import mixer as mx
def shoot():
    mx.Sound('audio/shoot_weapon.wav').play(-1, 100)

def ship_collision():
    mx.Sound('audio/ship_collision.wav').play(-1, 2000)

def bullet_hit():
    mx.Sound('audio/bullet_hit.wav').play(-1, 500)

def play_game():
    mx.Sound('audio/play_game.wav').play(-1, 2000)

def game_over():
    mx.Sound('audio/game_over.wav').play(-1, 1000)

