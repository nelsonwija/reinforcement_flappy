import pygame
from assets import BG_IMG, WIN_WIDTH, WIN_HEIGHT, STAT_FONT, GEN
from assets import Bird, Base, Pipe


def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)

    pygame.display.update()


def main():
    bird = Bird(230, 250)
    base = Base(730)
    pipes = [Pipe(600)]
    score = 0
    win = pygame.display.set_mode( (WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        bird.move()

        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pygame.quit()
                quit()
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        # quit game if bird hits the floor
        if bird.y + bird.img.get_height() >= 730:
            pygame.quit()
            break

        base.move()
        draw_window(win, bird, pipes=pipes, base=base, score=score)

    pygame.quit()
    quit()


main()
