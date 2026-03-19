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
	
	def on_pressed(self):
		pass

#Level Class
class Level(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		self.foods = pygame.sprite.Group()
		self.prohibited_foods = list(int)
	
	def add_food():
		pass

	def update(self):
		

		return super().update()

	def render(self, surface):
		for food in self.foods:
			surface.blit(food.image, food.rect)

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