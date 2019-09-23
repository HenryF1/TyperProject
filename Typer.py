import pygame

test_list = ['hello', 'like', 'size', 'write', 'yes','henry']


class Word(pygame.sprite.Sprite):
    def __init__(self, word_list):
        pygame.sprite.Sprite.__init__(self)

        self.word_counter = 0
        self.word_list = word_list
        self.font = pygame.font.Font('courier.ttf', 100)
        self.typed_letters = ''
        self.base_font_color = (0, 0, 0)
        self.correct_font_color = (0, 255, 0)
        self.incorrect_font_color = (255, 0, 0)
        self.text = []

    def update(self, key_pressed, *args):
        current_word = self.word_list[self.word_counter]

        if self.typed_letters != current_word:

            for char in key_pressed:
                if char != '0' and len(self.typed_letters) < len(current_word):
                    self.typed_letters += char
                elif char == '0':
                    self.typed_letters = self.typed_letters[:-1]

            self.text = [self.font.render(current_word, True, self.base_font_color)]

            for count in range(len(self.typed_letters)):
                if self.typed_letters[count] == current_word[count]:
                    self.text.append(self.font.render(self.typed_letters[count], True, self.correct_font_color))
                else:
                    self.text.append(self.font.render(self.typed_letters[count], True, self.incorrect_font_color))

        else:
            self.typed_letters = ''
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
                    if event.key == pygame.K_BACKSPACE:
                        press_key += '0'

            word_group.update(press_key)

            # game_screen.blit(bg, (0, 0))
            screen.fill((204, 255, 204))
            game_screen.blit(test.text[0], test.text[0].get_rect(center=(512, 250)))

            for letter in range(len(test.text) - 1):
                game_screen.blit(test.text[letter + 1],
                                 test.text[letter + 1].get_rect
                                 (center=(512 - (len(test.word_list[test.word_counter]) - 1)
                                          / 2 * 60 + letter * 60, 350)))

            pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((1024, 768))
Game().main(screen)