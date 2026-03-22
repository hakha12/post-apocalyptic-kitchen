import pygame, state, os

class GameOver(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		self.bg_image = pygame.image.load(os.path.join('assets','sprite', 'game_over.png'))
		self.bg_rect = self.bg_image.get_rect()
		self.bg_rect.topleft = ((0, 0))

		self.sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'Game Over.wav'))

		self.title_font = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixel Square Bold10.ttf'), 50)
		self.subtitle_font = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixel Square 10.ttf'), 20)
	
	def get_play_data(self, score: int, time: int):
		pass
	
	def awake(self):
		self.sound.play()
		return super().awake()
	
	def sleep(self):
		self.sound.stop()
		return super().sleep()

	def update(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_ESCAPE]:
			self.state_manager.set_only_current_state('Title')
		
		if key[pygame.K_SPACE]:
			self.state_manager.set_only_current_state('Level')
		
		return super().update()
	
	def render(self, surface):
		surface.fill((255, 255, 255))
		surface.blit(self.bg_image, self.bg_rect)

		title = self.title_font.render('GAME OVER', True, [255, 255, 255])
		subtitle = self.subtitle_font.render('Press SPACE to RESTART, or ESC to MAIN MENU', True, [255, 255, 255])
		surface.blit(title, (35, 480/2))
		surface.blit(subtitle, (35, 480/2 + 60))
		return super().render(surface)