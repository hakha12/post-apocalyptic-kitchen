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

		return super().render(surface)