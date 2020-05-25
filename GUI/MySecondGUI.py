import pygame
import pygame_gui as pgui

# Initialize PyGame
pygame.init()

# Set Window Title
pygame.display.set_caption('Thermal Cam')

# Create a surface
image = pygame.Surface((240, 240))


background = pygame.Surface((600, 400))
background.fill(pygame.Color('#e4e4e4'))


screen = pygame.display.set_mode((600, 400))



manager = pgui.UIManager((600, 400))

# Create 'Say Hello' button

start_button_rect = pygame.Rect((360, 262), (100, 50))
stop_button_rect  = pygame.Rect((480, 262), (100, 50))
image_rect        = pygame.Rect((350, 12), (240, 240))

start_button = pgui.elements.UIButton(relative_rect=start_button_rect, text='Start', manager=manager)
stop_button  = pgui.elements.UIButton(relative_rect=stop_button_rect, text='Stop', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        if event.type == pygame.USEREVENT:
            if event.user_type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                      print('Start sensor')
                      image.fill((0, 0, 0))
                      
                if event.ui_element == stop_button:
                      print('Stop sensor')
                      image.fill((255, 255, 255))
                      pygame.draw.rect(image, (255, 0, 0), image.get_rect(), 10)  # Draw on it.
                     
        manager.process_events(event)
        
    manager.update(time_delta)
            
    screen.blit(background, (0, 0))
    screen.blit(image, (350, 12))
    manager.draw_ui(screen)
    
    pygame.display.update()