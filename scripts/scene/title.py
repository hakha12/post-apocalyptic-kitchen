import pygame, state, os

class Title(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		self.bg_animations = [pygame.image.load(os.path.join('assets', 'sprite', 'title_1.png')),
					 	   				pygame.image.load(os.path.join('assets', 'sprite', 'title_2.png')),
						  				pygame.image.load(os.path.join('assets', 'sprite', 'title_3.png')),]
		
		self.animation_frame = 0
		self.bg_image = self.bg_animations[0]
		self.bg_rect = self.bg_image.get_rect()
		self.bg_rect.topleft = ((0, 0))

		self.title_font = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixel Square Bold10.ttf'), 50)
		self.subtitle_font = pygame.font.Font(os.path.join('assets', 'fonts', 'Pixel Square 10.ttf'), 20)

		self.sound_effect = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'Title Screen.wav'))

	def awake(self):
		self.sound_effect.play()
		return super().awake()
	
	def sleep(self):
		self.sound_effect.stop()
		return super().sleep()
	
	def update(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_SPACE]:
			self.state_manager.set_only_current_state('Level')

		if self.animation_frame == 2:
			self.animation_frame = 0
		else:
			self.animation_frame += 1
		
		self.bg_image = self.bg_animations[self.animation_frame]
		return super().update()
	
	def render(self, surface):
		surface.fill((255, 255, 255))
		surface.blit(self.bg_image, self.bg_rect)

		
		
		overlay = pygame.Surface((854, 480), pygame.SRCALPHA)
		overlay.fill((124, 63, 0, 120))
		surface.blit(overlay, (0, 0))

		title = self.title_font.render('WHAT SHOULD I DO HERE?', True, [255, 255, 255])
		subtitle = self.subtitle_font.render('Press SPACE to START', True, [255, 255, 255])
		surface.blit(title, (35, 480/2))
		surface.blit(subtitle, (35, 480/2 + 60))

		return super().render(surface)