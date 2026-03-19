import pygame, state, os

class Title(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)
	
	def render(self, surface):
		surface.fill((255, 255, 255))
		return super().render(surface)