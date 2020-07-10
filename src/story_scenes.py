from components.gamegui import Character, DialogueBox, ChoiceBox
from components.globalvar import scene_types, screen
from components.scene import Scene
w, h = screen.get_size()
s1 = Scene(screen,
           characters=[
               Character(screen, 'assets/Sayori1.png'),
               Character(screen, 'assets/Monika1.png'),
               Character(screen, 'assets/Yuri1.png'),
               Character(screen, 'assets/Natsuki1.png'),
           ],
           dialogue=DialogueBox(screen, 'Sayori', 'Play with meeee'),
           background_image='assets/Clubroom.png'
           )
s2 = Scene(screen,
           characters=[
               Character(screen, 'assets/Sayori1.png'),
               Character(screen, 'assets/Monika1.png'),
           ],
           dialogue=DialogueBox(screen, 'Sayori', 'Play with meeee'),
           )
choice_scene = Scene(screen,
           dialogue=DialogueBox(screen, None, 'Choose an option'),
           choicebox=ChoiceBox(screen, choices=['Sayori', 'Monika', 'Yuri', 'Natsuki']),
           scene_type=scene_types["CHOICES"]
           )
sayori_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Sayori1.png'),
    ],
    dialogue=DialogueBox(screen, 'Sayori', 'YAY Let\' play!'),
)
monika_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Monika1.png'),
    ],
    dialogue=DialogueBox(screen, 'Monika1', 'Just Monika'),
)
yuri_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Yuri1.png'),
    ],
    dialogue=DialogueBox(screen, 'Yuri', 'Thank you'),
)
natsuki_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Natsuki1.png'),
    ],
    dialogue=DialogueBox(screen, 'Natsuki', 'BAKA BAKA BAKA!'),
)

s1.next[0] = s2
s2.next[0] = choice_scene
choice_scene.next = {0: sayori_scene, 1: monika_scene, 2: yuri_scene, 3: natsuki_scene}
sayori_scene.next[0] = monika_scene.next[0] = yuri_scene.next[0] = natsuki_scene.next[0] = choice_scene