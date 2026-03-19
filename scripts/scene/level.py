import pygame, state, os

# Entity Class
class Food(pygame.sprite.Sprite):
	def __init__(self, type: int):
		super().__init__()

		self.image = None
		self.rect = self.image.get_rect()
		self.type = type

class Conveyor(pygame.sprite.Sprite):
	pass

class Presser(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super().__init__(*groups)

		self.animation_frames = [pygame.image.load(os.path.join('assets/sprite/presser_1.png')),
						  		 pygame.image.load(os.path.join('assets/sprite/presser_2.png')),
						  		 pygame.image.load(os.path.join('assets/sprite/presser_3.png')),]
		
		self.image = self.animation_frames[2]
		self.rect = self.image.get_rect()
		self.rect.top = 0
		self.rect.centerx = 854/2
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
	
	def on_pressed(self):
		pass

#Level Class
class Level(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		self.presser = Presser()
	
	def add_food():
		pass

	def update(self):


		return super().update()

	def render(self, surface):
		self.presser.render(surface)

		return super().render(surface)
	
	def on_pressed(self):
		pass


class Pause(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, True, False)
	
	def on_restart(self):
		pass

	def on_return(self):
		pass