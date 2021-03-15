class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        """Te canta la canción, te canta la canciooooooón!!!"""
        for line in self.lyrics:
            print(line)
        print("\n")
            
cumple = ["Cumple años feliz!",
               "Te deseamos todos!",
               "Cunple años feliz!"
               ]


cucaracha = ["La cucaracha, la cucaracha",
                  "Ya no puede caminar...",
                  "por que no tiene",
                  "por que le faltan",
                  "Las dos patitas de atras"]

canta_cumple = Song(cumple)

canta_cucaracha = Song(cucaracha)

canta_cumple.sing_me_a_song()
canta_cucaracha.sing_me_a_song()