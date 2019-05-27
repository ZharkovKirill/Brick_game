#Ядро игры
import  pygame
import brick
from pygame.locals import *
from matrix import field_ini

class Game:
    def __init__(self,seed_mat):
        self.seed_mat = seed_mat
        pygame.init()
        pygame.font.init()
        self.table = pygame.font.SysFont('Comic Sans MS', 20)
        self.table2 = pygame.font.SysFont('Comic Sans MS', 20)
        self.over = pygame.font.SysFont('Comic Sans MS', 50)
        self.swap_score = 0
        self.background = pygame.image.load('img/back2.jpg')
        self.end_ground = pygame.image.load('img/back.jpg')
        self.screen = pygame.display.set_mode((400, 400))
        self.blocks = brick.ini_blocks(seed_mat)
        self.loop = True
        self.clock = pygame.time.Clock()
        self.score = self.game_end()
        self.text_score = self.table.render(('Score:'+str(self.score)), False, (0, 0, 0))
        self.text_swaps = self.table2.render(('Swaps:'+str(self.swap_score)), False, (0, 0, 0))
        self.text_over =     self.over.render('Game over', False, (0, 0, 0))
        self.mouse_obj1 = 0
        self.mouse_obj2 = 0
        self.grab_flag = 0
    def game_end(self):
        s = 0
        for i in self.blocks:
            for j in range(3):
                if ((i.x == (100 + 80 * j)) and (i.role == (2 + j))):
                    s += 1
        return s
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for i in self.blocks:
            i.draw(self.screen)
        self.text_score =self.table.render(('Score:'+str(self.score)), False, (0, 0, 0))
        self.text_swaps = self.table2.render(('Swaps:' + str(self.swap_score)), False, (0, 0, 0))
        self.screen.blit(self.text_score, (10, 10))
        self.screen.blit(self.text_swaps, (305, 10))
        pygame.display.update()

        return
    def grab_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.loop = False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                self.clock.tick(5)
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    self.mouse_proc(pos)
    def mouse_proc(self,pos):
        pos = pygame.mouse.get_pos()
        self.mouse_obj1 = brick.colider(pos, self.blocks)
        if (self.grab_flag == 0) and (self.blocks[self.mouse_obj1].role > 1):
            self.mouse_obj2 = self.mouse_obj1
            self.blocks[self.mouse_obj1].image.set_alpha(150)
            self.grab_flag = 1
        elif ((self.grab_flag  == 1) and (self.blocks[self.mouse_obj1].role == 0)):
            if (brick.neighb(self.blocks[self.mouse_obj1],self.blocks[self.mouse_obj2])):
                self.swap_score =brick.swap_block(self.blocks, self.mouse_obj2, self.mouse_obj1,self.swap_score)
                self.score = self.game_end()

            self.blocks[self.mouse_obj2].image.set_alpha(255)
            k = 0
            self.grab_flag = 0
        elif (self.grab_flag  == 1) and (self.blocks[self.mouse_obj1].role > 0):
            self.blocks[self.mouse_obj2].image.set_alpha(255)
            self.grab_flag = 0
    def game_over(self):
        if self.score==15:
            self.screen.blit(self.end_ground,(0,0))
            self.screen.blit(self.text_over, (100, 200))
            pygame.display.update()
            pygame.time.delay(1000)
            self.loop = False
    def run(self):
        while(self.loop):
            self.game_over()
            self.grab_event()
            self.draw()
            self.clock.tick(60)


seed_matrix = field_ini()
gm = Game(seed_matrix)
gm.run()
