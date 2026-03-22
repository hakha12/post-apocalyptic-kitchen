import pygame, state, os

class GameOver(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		self.bg_image = pygame.image.load(os.path.join('assets','sprite', 'game_over.png'))
		self.bg_rect = self.bg_image.get_rect()
		self.bg_rect.topleft = ((0, 0))
	
	def update(self):
		
		return super().update()
	
	def render(self, surface):
		surface.fill((255, 255, 255))
		surface.blit(self.bg_image, self.bg_rect)
		return super().render(surface)