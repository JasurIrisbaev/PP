import pygame

tracks = [
    "music/track1.mp3",
    "music/track2.mp3"
]

current_track = 0


def play_track():
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()


def run_player():
    global current_track

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Music Player")

    font = pygame.font.SysFont(None, 40)

    running = True

    while running:
        screen.fill((255, 255, 255))

        text = font.render(f"Track {current_track + 1}", True, (0, 0, 0))
        screen.blit(text, (180, 130))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                # P = Play
                if event.key == pygame.K_p:
                    play_track()

                # S = Stop
                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()

                # N = Next
                elif event.key == pygame.K_n:
                    current_track = (current_track + 1) % len(tracks)
                    play_track()

                # B = Previous
                elif event.key == pygame.K_b:
                    current_track = (current_track - 1) % len(tracks)
                    play_track()

                # Q = Quit
                elif event.key == pygame.K_q:
                    running = False

    pygame.quit()


if __name__ == "__main__":
    run_player()