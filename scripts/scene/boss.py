import state, pygame, os, random

class Boss(state.StateManager):
	def __init__(self, event_manager):
		super().__init__(event_manager)

		default = Default(self, event_manager)
		angry = Angry(self, event_manager)
		happy = Happy(self, event_manager)

		self.register_state('Default', default)
		self.register_state('Angry', angry)
		self.register_state('Happy', happy)

		self.set_only_current_state('Default')

		self.patient_level = 10
		self.score = 0

		self.preference: int = random.randint(0, 3)
		print(self.preference)
	
	def get_preference(self) -> int:
		return self.preference
	
	def on_destroy_target_food(self):
		current_state = list(self.current_state.values())
		self.score += current_state[0].destroy_food(False)

		print(self.score)

	def on_destroy_prohibited_food(self):
		current_state = list(self.current_state.values())
		self.score += current_state[0].destroy_food(True)
		self.patient_level -= 1

	def on_ignore_food(self):
		self.patient_level -= 1

	def on_preference_change(self):
		self.preference = random.randint(0, 3)

class Default(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: return -3
		else: return 3

class Angry(state.State):
	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: return -6
		else: return 1

class Happy(state.State):
	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: return -1
		else: return 6

class Tutor(state.State):
	pass