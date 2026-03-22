import state, pygame, os, random

class Boss(state.StateManager):
	def __init__(self, event_manager):
		super().__init__(event_manager)

		pygame.BOSS_PREFERENCE_CHANGE = self.event_manager.add_user_event()

		default = Default(self, event_manager)
		angry = Angry(self, event_manager)
		happy = Happy(self, event_manager)

		self.register_state('Default', default)
		self.register_state('Angry', angry)
		self.register_state('Happy', happy)

		self.set_only_current_state('Default')

		self.animations = [pygame.image.load(os.path.join('assets','sprite', 'boss_1.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'boss_2.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'boss_3.png')),]
		
		self.animation_frame = 0

		self.image = self.animations[0]
		self.rect = self.image.get_rect()
		self.rect.bottomright = ((800, 322))

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

		if self.patient_level < 5:
			self.set_only_current_state('Angry')

		if self.patient_level == 0:
			self.event_manager.trigger_user_event(pygame.GAME_OVER)

	def on_preference_change(self):
		self.preference = random.randint(0, 3)

class Default(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.tolerance_count = 0
		self.praise_count = 0
	
	def awake(self):
		self.event_manager.set_timer(pygame.BOSS_PREFERENCE_CHANGE, 2500)
		return super().awake()

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited:
			self.tolerance_count += 1

			if self.tolerance_count > 2:
				self.tolerance_count = 0
				self.state_manager.set_only_current_state('Angry') 
			return -3
		else:
			self.praise_count += 1

			if self.praise_count > 2:
				self.praise_count = 0
				self.state_manager.set_only_current_state('Happy') 
			
			return 3

class Angry(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.tolerance_count = 0

		self.animations = [pygame.image.load(os.path.join('assets','sprite', 'angy_1.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'angy_2.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'angy_3.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'angy_4.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'angy_5.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'angy_6.png')),]
		
		self.animation_frame = 0

		self.image = self.animations[self.animation_frame]
		self.rect = self.image.get_rect()
		self.rect.center = [800, 200]

		self.praise_count = 0
	
	def awake(self):
		self.event_manager.set_timer(pygame.BOSS_PREFERENCE_CHANGE, 2000)
		return super().awake()
	
	def update(self):
		if self.animation_frame == 5:
			self.animation_frame = 0
		else:
			self.animation_frame += 1
		
		self.image = self.animations[self.animation_frame]
		return super().update()
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
		return super().render(surface)

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: 
			self.tolerance_count += 1

			if self.tolerance_count > 2:
				self.tolerance_count = 0
				self.event_manager.trigger_user_event(pygame.GAME_OVER)
			return -6
		else: 
			self.praise_count += 1

			if self.praise_count > 2:
				self.praise_count = 0
				self.state_manager.set_only_current_state('Happy') 
			
			return 1

class Happy(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, False, False)

		self.animations = [pygame.image.load(os.path.join('assets','sprite', 'happy_1.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'happy_2.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'happy_3.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'happy_4.png')),
					 	   pygame.image.load(os.path.join('assets','sprite', 'happy_5.png')),
						   pygame.image.load(os.path.join('assets','sprite', 'happy_6.png')),]
		
		self.animation_frame = 0

		self.image = self.animations[self.animation_frame]
		self.rect = self.image.get_rect()
		self.rect.center = [800, 200]
		self.tolerance_count = 0
	
	def awake(self):
		self.event_manager.set_timer(pygame.BOSS_PREFERENCE_CHANGE, 3500)
		return super().awake()
		
	
	def update(self):
		if self.animation_frame == 5:
			self.animation_frame = 0
		else:
			self.animation_frame += 1
		
		self.image = self.animations[self.animation_frame]
		return super().update()
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
		return super().render(surface)

	def destroy_food(self, is_prohibited: bool) -> int:
		if is_prohibited: 
			self.tolerance_count += 1

			if self.tolerance_count > 2:
				self.tolerance_count = 0
				self.state_manager.set_only_current_state('Default') 
			return -1
		else: 
			return 6

class Tutor(state.State):
	pass