import pygame
import pygame_gui as pgui

pygame.init()

pygame.display.set_caption('Thermal Cam')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#e4e4e4'))

manager = pgui.UIManager((800, 600))

# Create 'Say Hello' button
button_layout_rect = pygame.Rect(30, 20, 100, 20)
button_layout_rect.bottomright = (-30, -20)

hello_button = pgui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Start',
                                             manager=manager)

slider_1 = pgui.elements.UIHorizontalSlider(relative_rect = pygame.Rect((150, 375), (400, 20)),
                                            start_value = 5, value_range = (0, 10), manager=manager)

slider_2 = pgui.elements.UIHorizontalSlider(relative_rect = pygame.Rect((150, 475), (400, 20)),
                                            start_value = 5, value_range = (0, 10), manager=manager)

text_1   = pgui.elements.UITextBox(html_text = "MINTEMP", relative_rect = pygame.Rect((80, 475), (100, 100)),
                                   manager = manager, wrap_to_height = False, layer_starting_height = 1)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        if event.type == pygame.USEREVENT:
            if event.user_type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                      print('Hello World!')
                     
        manager.process_events(event)
        
    manager.update(time_delta)
            
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    
    pygame.display.update()