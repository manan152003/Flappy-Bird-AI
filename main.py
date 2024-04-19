import pygame, sys
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(200)

GEN = 0
FONT = pygame.font.SysFont("dejavuserif", 50)

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def generate_pipes():
    config.pipes.append(components.Pipes(config.WIN_WIDTH))

def main():
    pipes_spawn_time = 10
    while True:
        quit_game()

        config.window.fill((53,47,54))
        global GEN

        # Spawn Ground
        config.ground.draw(config.window)

        #spawning pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)

        
        #getting player (navghan)
        if not population.extinct():
            text = FONT.render("Gen: " + str(GEN+1), 1, (154,154,154))
            config.window.blit(text, (10, 10))
            population.update_live_players()    
        else:
            GEN += 1
            config.pipes.clear()
            population.natural_selection()

        clock.tick(60)
        pygame.display.flip()

main()