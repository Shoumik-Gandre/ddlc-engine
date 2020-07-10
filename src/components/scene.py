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
            w = self.screen.get_width()
            for i, obj in enumerate(self.characters):
                """
                The following line divides screen width-wise into "len(characters)" cells of equal width 
                and puts an object in the middle of the ith cell with a left shift of imagewidth/2 of that image of character
                """
                fit_mid_cell = (2*i + 1) * w // (2 * len(self.characters)) - obj.image.get_rect().width//2
                obj.position = (fit_mid_cell, obj.position[1])
                obj.draw()
        if self.dialogue:
            self.dialogue.draw()
        if self.choicebox:
            self.choicebox.draw()
