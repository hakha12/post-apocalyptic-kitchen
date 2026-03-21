import pygame, state, os, random
import scene.boss as boss

# Entity Class
class Food(pygame.sprite.Sprite):
	image_list = [pygame.image.load(os.path.join('assets', 'sprite', 'bread.png')),
					 	   pygame.image.load(os.path.join('assets', 'sprite', 'cake.png')),
						   pygame.image.load(os.path.join('assets', 'sprite', 'ice_cream.png')),
						   pygame.image.load(os.path.join('assets', 'sprite', 'juice.png')),]
	
	def __init__(self, type: int = 0):
		super().__init__()

		

		self.type = type

		self.image = Food.image_list[type]
		self.rect = self.image.get_rect()
		
		
		self.pos = pygame.math.Vector2((-100, 300))
		self.vel = pygame.math.Vector2()
	
	def update(self, *args, **kwargs):
		self.pos += self.vel

		return super().update(*args, **kwargs)
	
	def late_update(self):
		self.rect.center = self.pos
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
	
	def on_destroy_food(self):
		pass

class Conveyor(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super().__init__(*groups)

		self.animations = [pygame.image.load(os.path.join('assets', 'sprite', 'conveyor_1.png')),
						  		 pygame.image.load(os.path.join('assets', 'sprite', 'conveyor_2.png')),
						  		 pygame.image.load(os.path.join('assets', 'sprite', 'conveyor_3.png')),]
		
		self.animation_frame = 0

		self.image = self.animations[0]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = [0, 480]
	
	def update(self, *args, **kwargs):
		if self.animation_frame == 2:
			self.animation_frame = 0
		else:
			self.animation_frame += 1
		
		self.image = self.animations[self.animation_frame]

	def render(self, surface):
		surface.blit(self.image, self.rect)

class Presser(state.StateManager):
	def __init__(self, event_manager):
		super().__init__(event_manager)

		self.animations = [pygame.image.load(os.path.join('assets','sprite', 'presser_3.png')),
					 	   pygame.image.load(os.path.join('assets', 'sprite', 'presser_1.png')),
						   pygame.image.load(os.path.join('assets', 'sprite', 'presser_2.png')),]
		
		self.animation_frame = 0
		
		self.image = self.animations[0]
		self.rect = self.image.get_rect()
		self.rect.top = 0
		self.rect.centerx = 854/2

		self.is_pressed = False

		self.sound_effect = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'SFX 2.wav'))


	
	def update(self, *args, **kwargs):
		if self.is_pressed == True:
			self.animation_frame += 1
		
		self.image = self.animations[self.animation_frame]

		if self.animation_frame == 2:
			self.animation_frame = 0
			self.is_pressed = False
	
	def render(self, surface):
		surface.blit(self.image, self.rect)
	
	def check_food_collision(self, food_group: pygame.sprite.Group, preference: int):
		hit = pygame.sprite.spritecollide(self, food_group, False)

		if hit and self.is_pressed:
			hit[0].kill()

			if hit[0].type == preference:
				self.event_manager.trigger_user_event(pygame.DESTROY_TARGET_FOOD)
			else:
				self.event_manager.trigger_user_event(pygame.DESTROY_PROHIBITED_FOOD)

#Level Class
class Level(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager)

		pygame.mixer.music.load(os.path.join('assets', 'sounds', 'Gameplay.wav'))
		pygame.mixer.music.set_volume(0.5)

		self.boss = boss.Boss(event_manager)

		self.conveyor = Conveyor()
		self.presser = Presser(event_manager)

		self.foods = pygame.sprite.Group()
		preference = self.boss.get_preference()
		self.preference_food = Food().image_list[preference]
		self.preference_rect = self.preference_food.get_rect()
		self.preference_rect.topleft = ((30, 30))

		pygame.INSERT_FOOD = self.event_manager.add_user_event()
		pygame.DESTROY_TARGET_FOOD = self.event_manager.add_user_event()
		pygame.DESTROY_PROHIBITED_FOOD = self.event_manager.add_user_event()
		pygame.IGNORE_FOOD = self.event_manager.add_user_event()
		pygame.BOSS_PREFERENCE_CHANGE = self.event_manager.add_user_event()

		self.event_manager.add_callback(pygame.DESTROY_TARGET_FOOD, self.boss.on_destroy_target_food)
		self.event_manager.add_callback(pygame.DESTROY_PROHIBITED_FOOD, self.boss.on_destroy_prohibited_food)
		self.event_manager.add_callback(pygame.IGNORE_FOOD, self.boss.on_ignore_food)
		self.event_manager.add_callback(pygame.BOSS_PREFERENCE_CHANGE, self.boss.on_preference_change)
	
	def awake(self):
		self.event_manager.add_callback(pygame.INSERT_FOOD, self.on_insert_food)
		self.event_manager.set_timer(pygame.INSERT_FOOD, 1500)
		self.event_manager.set_timer(pygame.BOSS_PREFERENCE_CHANGE, 3500)

		pygame.mixer.music.play(-1)

		return super().awake()
	
	def sleep(self):
		return super().sleep()

	def update(self):
		self.boss.update()
		self.conveyor.update()

		key = pygame.key.get_pressed()

		if key[pygame.K_SPACE]:
			self.presser.sound_effect.play()
			self.presser.is_pressed = True
		preference = self.boss.get_preference()
		self.preference_food = Food().image_list[preference]
		self.presser.update()
		self.presser.check_food_collision(self.foods, preference)

		for food in self.foods:
			food.update()

		return super().update()
	
	def late_update(self):
		for food in self.foods:
			food.late_update()
		return super().late_update()

	def render(self, surface):
		surface.fill((0, 0, 0))
		self.boss.render(surface)
		surface.blit(self.preference_food, self.preference_rect)
		self.conveyor.render(surface)

		for food in self.foods:
			food.render(surface)

		self.presser.render(surface)

		return super().render(surface)
	
	def on_insert_food(self):
		type = random.randint(0, 3)
		food = Food(type)
		food.vel = pygame.math.Vector2(10, 0)

		self.foods.add(food)

	
		

class Pause(state.State):
	def __init__(self, manager, event_manager):
		super().__init__(manager, event_manager, True, False)
	
	def on_restart(self):
		pass

	def on_return(self):
		pass