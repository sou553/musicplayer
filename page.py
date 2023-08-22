import sys
import pygame
from pygame.locals import *
import folder


def change_page(page, track_num):
    if page == 0:
        select_music()
    if page == 1:
        play_music(track_num)


def select_music():
    pygame.init()
    (w, h) = 600, 900
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Select Page")


    tri_right = pygame.image.load("files/png/ui_png/tri_right.png").convert_alpha()
    rect_tri_right = tri_right.get_rect()
    rect_tri_right.center = (450, 760)
    tri_left = pygame.image.load("files/png/ui_png/tri_left.png").convert_alpha()
    rect_tri_left = tri_left.get_rect()
    rect_tri_left.center = (150, 760)

    music_names = folder.get_musicname()

    c = 0
    for title in music_names:#title_font = pygame.font.SysFont("hg正楷書体pro", 50)
        exec("title_font_" + str(c) + "= pygame.font.SysFont(" + "\"hg正楷書体pro\"" + ", 30)")
        exec("title_text_" + str(c) + "= title_font_" + str(c) + ".render(title, True, (255, 255, 255))")
        c += 1

    title_x = 20
    n = int(len(music_names) / 15)
    m = (len(music_names) % 15)
    page = 0
    if m == 0: 
        page_max = n
    else:
        page_max = n+1
    

    while True:
        screen.fill((0, 0, 0, 0))#背景色の指定
        screen.blit(tri_right, rect_tri_right)
        screen.blit(tri_left, rect_tri_left)
        c = page * 15
        title_y = 50
        if page != (page_max-1):
            for i in range(15):
                exec("screen.blit(title_text_" + str(c) + ", (" + str(title_x) + "," + str(title_y) + "))")
                c += 1
                title_y += 45
        else:
            for i in range(m):
                exec("screen.blit(title_text_" + str(c) + ", (" + str(title_x) + "," + str(title_y) + "))")
                c += 1
                title_y += 45

        pygame.time.wait(10) #更新間隔
        pygame.display.update() #画面更新

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 125 <= x and 175 >= x and 745 <= y and 775 >= y:
                    page = ((page-1)%page_max)
                if 430 <= x and 480 >= x and 745 <= y and 775 >= y:
                    page = ((page+1)%page_max)
                
                for i in range(15):
                    if (55 + 45 * i) <= y and (75 + 45 * i) >= y:
                        if 0 <= (page*15+i) and len(music_names) > (page*15+i):
                            track = page*15+i
                            play_music(track)



def play_music(current_track = 0):
    pygame.mixer.init()
    pygame.init()

    music_filenames = folder.get_musicfilename()
    music_names = folder.get_musicname()
    max_tracks = len(music_filenames)

    (w, h) = 600, 900
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Play Page")
    
    tri_right = pygame.image.load("files/png/ui_png/tri_right.png").convert_alpha()
    rect_tri_right = tri_right.get_rect()
    rect_tri_right.center = (450, 700)
    tri_left = pygame.image.load("files/png/ui_png/tri_left.png").convert_alpha()
    rect_tri_left = tri_left.get_rect()
    rect_tri_left.center = (150, 700)
    back = pygame.image.load("files/png/ui_png/tri_left.png").convert_alpha()
    rect_back = back.get_rect()
    rect_back.center = (50, 100)

    title_x = 200
    title_y = 500

    pygame.mixer.music.load(music_filenames[current_track])
    pygame.mixer.music.play(1)

    clock = pygame.time.Clock()
    
    playing = True
    paused = False

    TRACK_END = USEREVENT + 1
    pygame.mixer.music.set_endevent(TRACK_END)

    while True:
        title_font = pygame.font.SysFont("hg正楷書体pro", 50)
        title_text = title_font.render(music_names[current_track], True, (255, 255, 255))
        title_size = len(music_names[current_track]) * 25
        title_x -= 1
        if title_x < -(title_size + 50):
            title_x = 200
        
        if paused:
            playback = pygame.image.load("files/png/ui_png/playback.png").convert_alpha()
            rect_playback = playback.get_rect()
            rect_playback.center = (300, 700)
        else:
            playback = pygame.image.load("files/png/ui_png/pose.png").convert_alpha()
            rect_playback = playback.get_rect()
            rect_playback.center = (300, 700)
        screen.fill((0, 0, 0, 0)) #背景色の指定
        screen.blit(tri_right, rect_tri_right)
        screen.blit(tri_left, rect_tri_left)
        screen.blit(playback, rect_playback)
        screen.blit(back, rect_back)
        screen.blit(title_text, (title_x, title_y))
    

        pygame.time.wait(10) #更新間隔
        pygame.display.update() #画面更新
    
        button_pressed = None

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if 25 <= x and 75 >= x and 85 <= y and 115 >= y:
                    select_music()
                if 125 <= x and 175 >= x and 685 <= y and 715 >= y:
                    button_pressed = "prev"
                if 430 <= x and 480 >= x and 685 <= y and 715 >= y:
                    button_pressed = "next"
                if 270 <= x and 335 >= x and 665 <= y and 735 >= y:
                    if paused:
                        button_pressed = "play"
                    else:
                        button_pressed = "pause" 


            
            if event.type == TRACK_END:
                button_pressed = "next"

        if button_pressed != None:
            if button_pressed == "next":
                current_track = (current_track + 1) % max_tracks
                pygame.mixer.music.load(music_filenames[current_track])            
                pygame.mixer.music.play()
                title_x = 200
                paused = False

            elif button_pressed == "prev":
                if pygame.mixer.music.get_pos() > 3000:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                else:
                    current_track = (current_track - 1) % max_tracks
                    pygame.mixer.music.load(music_filenames[current_track])            
                    pygame.mixer.music.play()
                    title_x = 200
                    paused = False

            elif button_pressed == "pause":
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            
            elif button_pressed == "stop":#いらんかもしれん
                pygame.mixer.music.stop()
                playing = False

            elif button_pressed == "play":
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False


if __name__ == "__main__":
    select_music()