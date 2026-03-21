import pygame

class EventManager():
	def __init__(self):
		self.user_event_count = 0

		self.callback_list: dict[int, list] = {}

	def add_user_event(self) -> int:
		self.user_event_count += 1

		return pygame.USEREVENT + self.user_event_count
	
	def trigger_user_event(self, event_type: int):

		event = pygame.event.Event(event_type)
		pygame.event.post(event)

	def add_callback(self, event: int, callback):
		# TO DO: Check if the user event already exist
		
		callback_list = self.callback_list.setdefault(event, [])

		if callback in callback_list: return

		callback_list.append(callback)
	
	def remove_callback(self, event: int, callback):
		callback_list = self.callback_list.setdefault(event, [])

		if callback not in callback_list: return

		callback_list.pop(callback)
		
	def set_timer(self, event: int, time: int):
		pygame.time.set_timer(event, time)

	def update(self):
		for event in pygame.event.get():
			if event.type not in self.callback_list: continue

			callback_list = self.callback_list.get(event.type)

			for callback in callback_list: callback()