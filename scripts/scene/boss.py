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

		self.animations = [pygame.image.load(os.path.join('assets','sprite', 'boss_1.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'boss_2.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'boss_1.png')),]
		
		self.animation_frame = 0

		self.image = self.animations[0]
		self.rect = self.image.get_rect()
		self.rect.bottomright = ((840, 325))

		self.patient_level = 10
		self.score = 0

		self.preference: int = random.randint(0, 3)
		
		print(self.preference)
	
	def update(self):
		if self.animation_frame == 2:
			self.animation_frame = 0
		else:
			self.animation_frame += 1
		
		self.image = self.animations[self.animation_frame]

		return super().update()
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
		return super().render(surface)
	
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

		print(self.score)

	def on_ignore_food(self):
		self.patient_level -= 1

	def on_preference_change(self):
		self.preference = random.randint(0, 3)

class Default(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.tolerance_count = 0
		self.praise_count = 0

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited:
			self.praise_count += 1

			if self.praise_count_count > 2:
				self.praise_count_count = 0
				self.state_manager.set_only_current_state('HAPPY') 
			return -3
		else:
			self.tolerance_count += 1

			if self.tolerance_count > 2:
				self.tolerance_count = 0
				self.state_manager.set_only_current_state('ANGRY') 
			return 3

class Angry(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.tolerance_count = 0

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: return -6
		else: return 1

class Happy(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.tolerance_count = 0

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: return -1
		else: return 6

class Tutor(state.State):
	pass