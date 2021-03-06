"""
This File contains how we interact with everything.
"""

import pygame
from components.globalvar import scene_types, screen
from story_scenes import s1


def game_loop():
    pygame.init()
    pygame.display.set_caption("DDLC")

    run = True
    scene = s1
    screen.fill((0, 0, 0))
    scene.draw()
    pygame.display.update()
    while run:

        # screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if scene.scene_type == scene_types["NORMAL"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        scene = scene.next[0]
                    screen.fill((0, 0, 0))
                    scene.draw()
                    pygame.display.update()
            elif scene.scene_type == scene_types["CHOICES"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        scene = scene.next[scene.choicebox.selected_choice]
                    elif event.key == pygame.K_DOWN:
                        scene.choicebox.selected_choice = \
                            (scene.choicebox.selected_choice + 1) % len(scene.choicebox.choices)
                    elif event.key == pygame.K_UP:
                        scene.choicebox.selected_choice = \
                            (scene.choicebox.selected_choice - 1) % len(scene.choicebox.choices)
                    screen.fill((0, 0, 0))
                    scene.draw()
                    pygame.display.update()
            elif scene.scene_type == scene_types["CUTSCENE"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        scene = scene.next[0]
                    screen.fill((0, 0, 0))
                    scene.draw()
                    pygame.display.update()

        # scene.draw()
        # pygame.display.update()


game_loop()
