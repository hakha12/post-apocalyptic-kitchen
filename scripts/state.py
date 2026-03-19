import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite

import event_manager as em

class State(Sprite):
	def __init__(self, manager: StateManager, event_manager: em.EventManager, transparency: bool = False, transcendency: bool = False):
		super().__init__()

		self.state_manager = manager
		self.event_manager = event_manager
		
		self.is_transparent = transparency
		self.is_transcendent = transcendency
	
	def destroy(self):
		pass

	def awake(self):
		pass

	def sleep(self):
		pass

	def update(self):
		pass
	
	def late_update(self):
		pass

	def render(self, surface: pygame.Surface):
		if not hasattr(self, "image") and not hasattr(self, "rect"): return

		surface.blit(self.image, self.rect)
	

class StateManager(Sprite):
	def __init__(self, event_manager: em.EventManager):
		super().__init__()

		self.event_manager = event_manager

		self.state_list: dict[str, State] = dict()
		self.current_state: dict[str, State] = dict()
	
	def register_state(self, state_type: str, state_state: State):
		self.state_list[state_type] = state_state

	def add_state_to_current(self, state_type: str):
		state = self.state_list.get(state_type)

		if state_type in self.current_state: return
			
		self.current_state[state_type] = state
			
		state.awake()
	
	def set_only_current_state(self, state_type: str):
		state = self.state_list.get(state_type)

		if state_type in self.current_state: return

		self.current_state.clear()
		self.add_state_to_current(state_type)

	def remove_state_from_current(self, state_type: str):
		state = self.state_list.get(state_type)

		state.sleep()
		self.current_state.pop(state_type)

	def update(self):
		if self.current_state == None: return

		current_state = list(self.current_state.values())

		start_index = 0
		for i in range(len(current_state) - 1, -1, -1):
			if not current_state[i].is_transcendent: 
				start_index = i
				break

		for state in current_state[start_index:]:
			state.update()

	def late_update(self):
		if self.current_state == None: return

		current_state = list(self.current_state.values())

		start_index = 0
		for i in range(len(current_state) - 1, -1, -1):
			if not current_state[i].is_transcendent: 
				start_index = i
				break

		for state in current_state[start_index:]:
			state.late_update()
			
			if hasattr(state, "rect"): self.rect = state.rect

	def render(self, surface: pygame.Surface):
		if self.current_state == None: return

		current_state = list(self.current_state.values())

		start_index = 0
		for i in range(len(current_state) - 1, -1, -1):
			if not current_state[i].is_transparent: 
				start_index = i
				break

		for state in current_state[start_index:]:
			state.render(surface)