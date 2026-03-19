import pygame, state, os

class Intro(state.State):
	def __init__(self, manager: state.StateManager, event_manager:state.em.EventManager):
		super().__init__(manager, event_manager)

		pygame.INTRO_COUNTDOWN = self.event_manager.add_user_event()
		

		
		self.event_manager.set_timer(pygame.INTRO_COUNTDOWN, 2000)

		self.logo = pygame.image.load(os.path.join('assets','sprite','pygame_tiny.png'))
		self.logo_rect = self.logo.get_rect()

		self.logo_rect.center = (854/2, 480/2)
	
	def awake(self):
		self.event_manager.add_callback(pygame.INTRO_COUNTDOWN, self.on_countdown)

		return super().awake()
	
	def sleep(self):
		self.event_manager.remove_callback(pygame.INTRO_COUNTDOWN, self.on_countdown)

		return super().sleep()
	
	def update(self):
		return super().update()
	
	def render(self, surface):
		surface.blit(self.logo, self.logo_rect)

		return super().render(surface)
	
	def on_countdown(self):
		self.event_manager.set_timer(pygame.INTRO_COUNTDOWN, 0)

		self.state_manager.set_only_current_state("Level")