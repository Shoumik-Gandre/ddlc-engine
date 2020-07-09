from components.gamegui import Character, DialogueBox, ChoiceBox
from components.globalvar import scene_types, screen
from components.scene import Scene

s1 = Scene(screen,
           characters=[
               Character(screen, 'assets/Sayori1.png', (100, 300)),
               Character(screen, 'assets/Mon1.png', (200, 300)),
               Character(screen, 'assets/Yuri1.png', (300, 300)),
               Character(screen, 'assets/Natsuki1.png', (400, 300)),
           ],
           dialogue=DialogueBox(screen, 'Sayori', 'Play with meeee'),
           background_image='assets/Clubroom.png'
           )
s2 = Scene(screen,
           characters=[
               Character(screen, 'assets/Sayori1.png', (100, 300)),
               Character(screen, 'assets/Mon1.png', (200, 300)),
           ],
           dialogue=DialogueBox(screen, 'Sayori', 'Play with meeee'),
           )
choice_scene = Scene(screen,
           dialogue=DialogueBox(screen, '', 'Choose an option'),
           choicebox=ChoiceBox(screen, choices=['Sayori', 'Monica', 'Yuri', 'Natsuki']),
           scene_type=scene_types["CHOICES"]
           )
sayori_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Sayori1.png', (100, 300)),
    ],
    dialogue=DialogueBox(screen, 'Sayori', 'YAY Let\' play!'),
)
monica_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Mon1.png', (100, 300)),
    ],
    dialogue=DialogueBox(screen, 'Monica', 'Just Monica'),
)
yuri_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Yuri1.png', (100, 300)),
    ],
    dialogue=DialogueBox(screen, 'Yuri', 'Thank you'),
)
natsuki_scene = Scene(screen,
    characters=[
        Character(screen, 'assets/Natsuki1.png', (100, 300)),
    ],
    dialogue=DialogueBox(screen, 'Natsuki', 'BAKA BAKA BAKA!'),
)

s1.next[0] = s2
s2.next[0] = choice_scene
choice_scene.next = {0: sayori_scene, 1: monica_scene, 2: yuri_scene, 3: natsuki_scene}
sayori_scene.next[0] = monica_scene.next[0] = yuri_scene.next[0] = natsuki_scene.next[0] = choice_scene