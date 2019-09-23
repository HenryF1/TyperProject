import pygame

test_list = ['hello', 'like', 'size', 'write', 'yes','henry']


class Word(pygame.sprite.Sprite):
    def __init__(self, word_list):
        pygame.sprite.Sprite.__init__(self)

        self.word_counter = 0
        self.word_list = word_list
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        self.typed_letters = ''
        self.font_color = (0, 0, 0)
        self.text = []

    def update(self, key_pressed, *args):
        if len(self.typed_letters) != len(self.word_list[self.word_counter]):
            if key_pressed == self.word_list[self.word_counter][len(self.typed_letters)]:
                self.typed_letters += key_pressed

            self.text = [self.font.render(self.word_list[self.word_counter], True, self.font_color),
                         self.font.render(self.typed_letters, True, (255, 0, 0))]
        else:
            self.typed_letters = ""
            if self.word_counter + 1 == len(self.word_list):
                self.word_counter = 0
            else:
                self.word_counter += 1



class Game:
    def main(self, game_screen):
        clock = pygame.time.Clock()
        bg = pygame.transform.scale(pygame.image.load('cool_dog.jpg'), screen.get_size())
        word_group = pygame.sprite.Group()
        test = Word(test_list)
        word_group.add(test)

        while True:
            clock.tick(20)

            press_key = ''

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        press_key += 'q'
                    if event.key == pygame.K_w:
                        press_key += 'w'
                    if event.key == pygame.K_e:
                        press_key += 'e'
                    if event.key == pygame.K_r:
                        press_key += 'r'
                    if event.key == pygame.K_t:
                        press_key += 't'
                    if event.key == pygame.K_y:
                        press_key += 'y'
                    if event.key == pygame.K_u:
                        press_key += 'u'
                    if event.key == pygame.K_i:
                        press_key += 'i'
                    if event.key == pygame.K_o:
                        press_key += 'o'
                    if event.key == pygame.K_p:
                        press_key += 'p'
                    if event.key == pygame.K_a:
                        press_key += 'a'
                    if event.key == pygame.K_s:
                        press_key += 's'
                    if event.key == pygame.K_d:
                        press_key += 'd'
                    if event.key == pygame.K_f:
                        press_key += 'f'
                    if event.key == pygame.K_g:
                        press_key += 'g'
                    if event.key == pygame.K_h:
                        press_key += 'h'
                    if event.key == pygame.K_j:
                        press_key += 'j'
                    if event.key == pygame.K_k:
                        press_key += 'k'
                    if event.key == pygame.K_l:
                        press_key += 'l'
                    if event.key == pygame.K_z:
                        press_key += 'z'
                    if event.key == pygame.K_x:
                        press_key += 'x'
                    if event.key == pygame.K_c:
                        press_key += 'c'
                    if event.key == pygame.K_v:
                        press_key += 'v'
                    if event.key == pygame.K_b:
                        press_key += 'b'
                    if event.key == pygame.K_n:
                        press_key += 'n'
                    if event.key == pygame.K_m:
                        press_key += 'm'

            word_group.update(press_key)

            game_screen.blit(bg, (0, 0))

            for lines in range(len(test.text)):
                game_screen.blit(test.text[lines], test.text[lines].get_rect(center=(512, 250 + lines * 100)))

            pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((1024, 768))
Game().main(screen)