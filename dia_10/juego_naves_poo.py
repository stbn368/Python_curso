import pygame
import random
import math


class Config:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    PLAYER_SPEED = 0.5
    ENEMY_SPEED = 0.6
    BULLET_SPEED = 1.5
    COLLISION_DISTANCE = 27


class Game:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("Invasión Espacial")
        self.icon = pygame.image.load("icono_juego.png")
        pygame.display.set_icon(self.icon)
        self.background = pygame.image.load("fondo.jpg")
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.game_over_font = pygame.font.Font("freesansbold.ttf", 50)

        # Instanciar componentes
        self.player = Player()
        self.enemies = [Enemy() for _ in range(8)]
        self.bullet = Bullet()
        self.score = 0
        self.running = True

    def show_score(self):
        score_text = self.font.render(f"Puntuación: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def show_game_over(self):
        game_over_text = self.game_over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(game_over_text, (250, 200))

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.player.handle_input(event, self.bullet)

            self.player.update()
            self.bullet.update()

            for enemy in self.enemies:
                if enemy.update(self.bullet):
                    self.score += 1
                if enemy.y > 450:
                    self.show_game_over()
                    self.running = False
                    break

            self.player.draw(self.screen)
            self.bullet.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            self.show_score()
            pygame.display.update()


class Player:
    def __init__(self):
        self.image = pygame.image.load("cohete.png")
        self.x = Config.SCREEN_WIDTH // 2 - 32
        self.y = Config.SCREEN_HEIGHT - 100
        self.x_change = 0

    def handle_input(self, event, bullet):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -Config.PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                self.x_change = Config.PLAYER_SPEED
            if event.key == pygame.K_SPACE and not bullet.visible:
                bullet.fire(self.x, self.y)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.x_change = 0

    def update(self):
        self.x += self.x_change
        if self.x < 0:
            self.x = 0
        if self.x > Config.SCREEN_WIDTH - 64:
            self.x = Config.SCREEN_WIDTH - 64

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Enemy:
    def __init__(self):
        self.image = pygame.image.load("nave_extraterrestre.png")
        self.x = random.randint(0, Config.SCREEN_WIDTH - 64)
        self.y = random.randint(50, 200)
        self.x_change = Config.ENEMY_SPEED
        self.y_change = 30

    def update(self, bullet):
        self.x += self.x_change
        if self.x < 0:
            self.x_change = Config.ENEMY_SPEED
            self.y += self.y_change
        if self.x > Config.SCREEN_WIDTH - 64:
            self.x_change = -Config.ENEMY_SPEED
            self.y += self.y_change

        if self.check_collision(bullet):
            self.reset()
            bullet.reset()
            return True
        return False

    def check_collision(self, bullet):
        distance = math.sqrt((self.x - bullet.x)**2 + (self.y - bullet.y)**2)
        return distance < Config.COLLISION_DISTANCE and bullet.visible

    def reset(self):
        self.x = random.randint(0, Config.SCREEN_WIDTH - 64)
        self.y = random.randint(50, 200)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self):
        self.image = pygame.image.load("bala.png")
        self.x = 0
        self.y = Config.SCREEN_HEIGHT - 100
        self.y_change = Config.BULLET_SPEED
        self.visible = False

    def fire(self, player_x, player_y):
        self.visible = True
        self.x = player_x + 16
        self.y = player_y

    def update(self):
        if self.visible:
            self.y -= self.y_change
            if self.y < 0:
                self.reset()

    def reset(self):
        self.y = Config.SCREEN_HEIGHT - 100
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))


if __name__ == "__main__":
    game = Game()
    game.run()
