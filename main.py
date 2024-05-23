import pygame
import time
import random
import sys

class Game():
    def __init__(self):
        pygame.init()

        window_width = 300
        window_height = 300
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Snake Game")

        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(0, 255, 0)

        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        food_position = [random.randrange(1, (window_width // 10)) * 10,
                        random.randrange(1, (window_height // 10)) * 10]
        food_spawn = True

        clock = pygame.time.Clock()

        direction = 'RIGHT'
        change_to = direction
        score = 0

        def game_over():
            game_over_font = pygame.font.SysFont('Arial', 48)
            game_over_text = game_over_font.render('Game Over', True, red) if score < 10 else game_over_font.render('You Win!', True, red)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.midtop = (window_width / 2, window_height / 4)

            score_font = pygame.font.SysFont('Arial', 24)
            score_text = score_font.render('Score: ' + str(score), True, red)
            score_rect = score_text.get_rect()
            score_rect.midtop = (window_width / 2, window_height / 2)

            window.blit(game_over_text, game_over_rect)
            window.blit(score_text, score_rect)
    
            exit_button = pygame.Rect(window_width / 2 - 50, window_height / 1.5, 100, 50)
            pygame.draw.rect(window, red, exit_button)
            exit_font = pygame.font.SysFont('Arial', 24)
            exit_text = exit_font.render('Exit', True, white)
            exit_rect = exit_text.get_rect()
            exit_rect.center = exit_button.center
            window.blit(exit_text, exit_rect)

            pygame.display.flip()
            time.sleep(2)
            pygame.quit()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        change_to = 'RIGHT'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        change_to = 'LEFT'
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        change_to = 'DOWN'

            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'

            # Update the snake position
            if direction == 'RIGHT':
                snake_position[0] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10

            # Snake body mechanism
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
                score += 1
                food_spawn = False
            else:
                snake_body.pop()

            # Spawn new food
            if not food_spawn:
                food_position = [random.randrange(1, (window_width // 10)) * 10,
                                random.randrange(1, (window_height // 10)) * 10]
            food_spawn = True

            # Draw the snake and food
            window.fill(black)
            for pos in snake_body:
                pygame.draw.rect(window, green, pygame.Rect(
                    pos[0], pos[1], 10, 10))
            pygame.draw.rect(window, red, pygame.Rect(
                food_position[0], food_position[1], 10, 10))

            # Game over conditions
            if snake_position[0] < 0 or snake_position[0] > window_width - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_height - 10:
                game_over()
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()

            # Update the game display
            pygame.display.update()

            # Set the game speed
            clock.tick(15)

if __name__ == "__main__":
    Game()