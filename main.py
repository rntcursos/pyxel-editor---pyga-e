import pygame, sys
from scripts.buttons import Button
from scripts.color_indicator import Color_indicator
from scripts.pixel import Pixel
from scripts.settings import *
from scripts.text import Text
from scripts.text_input import Text_input
from scripts.ui import Ui

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pixel Editor')

running = True

#Groups
all_pixels = pygame.sprite.Group()
ui_group = pygame.sprite.Group()
all_colors = pygame.sprite.Group()

#Canvas Settings
resolution = 80
canvas = Ui((resolution,resolution),[0,0],PRIMARY_COLOR, ui_group)
tools_bar = Ui((200, screen.get_height()), [0,0],SECONDARY_COLOR, ui_group)
color_bar = Ui((screen.get_width(), 30), [0,0],PRIMARY_COLOR, ui_group)

#Pencil Settings
pencil_size = canvas.image.get_width() / resolution
pencil_color = "white"

#Tools Name
tools_name = "pencil"

#Texts
tool_text = Text(20,"Tool: " + tools_name, "white", [40,186], ui_group)

text_field_size = Text_input([40,140,128,30], tools_bar.image, ui_group)
text_field_size_label = Text(20,"Image size", "white", [40,116], ui_group)

text_field_pixels = Text_input([40,80,128,30], tools_bar.image, ui_group)
text_field_pixels_label = Text(20,"Pixels", "white", [40,56], ui_group)

def pencil_func():
    global tools_name
    tools_name = "pencil"
    tool_text.update_text("Tool: " + tools_name)

def eraser_func():
    global tools_name
    tools_name = "eraser"
    tool_text.update_text("Tool: " + tools_name)

def color_select_func():
    global tools_name
    tools_name = "color_select"
    tool_text.update_text("Tool: " + tools_name)

def save_func():
    size = int(text_field_size.value)
    canvas_save = pygame.transform.scale(canvas.image, [size, size])
    pygame.image.save(canvas_save, "assets/image.png")

def fill_func():
    global pencil_color
    canvas.image.fill(pencil_color)
    all_pixels.empty()

def clear_func():
    canvas.image.fill(PRIMARY_COLOR)
    all_pixels.empty()

pencil_button = Button("assets/brush.png",[40,210],pencil_func, ui_group)
eraser_button = Button("assets/eraser.png",[118,210],eraser_func, ui_group)
fill_button = Button("assets/fill.png",[40,285],fill_func, ui_group)
color_select_button = Button("assets/color_select.png",[118,285],color_select_func, ui_group)
save_button = Button("assets/save.png",[40,360],save_func, ui_group)
clear_button = Button("assets/clear.png",[118,360],clear_func, ui_group)

color_indicator = Color_indicator(pencil_color, [80,440], ui_group)


#Genereted Color Buttons
for x, c in enumerate(COLOR_LIST):
    x = x * 30
    Pixel(color_bar.image, c, [x, 0,30,30], all_colors)

def events():
    
    global pencil_size
    global pencil_color
    global tools_name
    global resolution
    
    x = pygame.mouse.get_pos()[0] - canvas.rect.x
    y = pygame.mouse.get_pos()[1] - canvas.rect.y
    key = pygame.mouse.get_pressed()

    click_x = x - (x % pencil_size) 
    click_y = y - (y % pencil_size)

    if tools_name == "pencil":
        if key[0]:
            resolution = int(text_field_pixels.value)
            pencil_size = canvas.image.get_width() / resolution
            Pixel(canvas.image, pencil_color, [click_x, click_y, pencil_size, pencil_size], all_pixels)
    elif tools_name == "eraser":
        if key[0]:
            resolution = int(text_field_pixels.value)
            pencil_size = canvas.image.get_width() / resolution
            Pixel(canvas.image, PRIMARY_COLOR, [click_x, click_y, pencil_size, pencil_size], all_pixels)
    elif tools_name == "color_select":
        for p in all_pixels:
            if p.rect.collidepoint(click_x, click_y):
                if key[0]:
                    pencil_color = p.color
                    tools_name = "pencil"
                    color_indicator.image.fill(pencil_color)


    if key[1]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        canvas.rect.topleft = (x - canvas.image.get_width() / 2, y - canvas.image.get_height() / 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        text_field_size.events_handle(event)
        text_field_pixels.events_handle(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                canvas.image = pygame.transform.scale(canvas.image, [canvas.image.get_width() * 2, canvas.image.get_height() * 2])
                pencil_size = canvas.image.get_width() / resolution
            elif event.button == 5:
                canvas.image = pygame.transform.scale(canvas.image, [canvas.image.get_width() / 2, canvas.image.get_height() / 2])
                pencil_size = canvas.image.get_width() / resolution
            
            

            for c in all_colors:
                if c.rect.collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        pencil_color = c.color
                        color_indicator.color_update(pencil_color)

def canvas_limit():

    if canvas.rect.y < color_bar.rect.height:
        canvas.rect.y = color_bar.rect.height
    
    if canvas.rect.x < tools_bar.rect.width:
        canvas.rect.x = tools_bar.rect.width

while running:
    
    events()
    canvas_limit()
    
    screen.fill((BG_COLOR))
        
    ui_group.draw(screen)
    ui_group.update()

    pygame.display.update()

