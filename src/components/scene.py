import pygame


class Scene(object):

    def __init__(self, screen, characters=[], dialogue=None, choicebox=None, background_image='assets/Clubroom.png', scene_type=0):
        self.scene_type = scene_type
        self.background = None
        if background_image:
            self.background = pygame.image.load(background_image)
        self.screen = screen
        self.dialogue = dialogue
        self.choicebox = choicebox
        self.characters = characters
        self.next = {0: None}

    def compute_optimal_pos(self):
        w = self.screen.get_width()
        sizes = round(w / len(self.characters))
        return sizes

    def draw(self):
        if self.background:
            self.screen.blit(self.background, self.background.get_rect())
        if self.characters:
            dist = self.compute_optimal_pos()
            for i, obj in enumerate(self.characters):
                obj.position = (dist*i, obj.position[1])
                obj.draw()
        if self.dialogue:
            self.dialogue.draw()
        if self.choicebox:
            self.choicebox.draw()
