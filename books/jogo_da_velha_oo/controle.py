# -*- coding: UTF-8 -*-
"""
Módulo responsável por controlar as ações do jogo
"""
import sys
class Controle(object):

    def __init__(self, stdscr):
        self.stdscr = stdscr
        stdscrwidth = stdscr.getmaxyx()[1]
        self.x_center = (stdscrwidth - 1) // 2
        self.pos_x = 0
        self.pos_y = 0
        self.entrada = None
    
    def _limites(self):

        if self.pos_x > 2:
            self.pos_x = 0
        elif self.pos_x < 0:
            self.pos_x = 2
            
        if self.pos_y > 2:
            self.pos_y = 0
        elif self.pos_y < 0:
            self.pos_y = 2

    def espaco_do_tabuleiro(self):

        self.entrada = self.stdscr.getkey()
        match self.entrada:
            case 'q':
                sys.exit(0)
            case 'a':
                self.pos_x -= 1
            case 'd':
                self.pos_x += 1
            case 's' :
                self.pos_y += 1
            case 'w' :
                self.pos_y -= 1
            case _:
                pass
            
        self.limites()
    
    def cursor(self):

        cursor_y = 9
        cursor_x = self.x_center - 3
       
        if self.pos_y == 1:
            cursor_y += 2
        elif self.pos_y == 2:
            cursor_y += 4
        
        if self.pos_x == 1:
            cursor_x += 2
        elif self.pos_x == 2:
            cursor_x += 4
        
        self.stdscr.move(cursor_y, cursor_x)
