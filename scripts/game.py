import scene_manager as scene
import event_manager as em
import sys, pygame

class Game():
	def __init__(self, fps: int = 60):
		pygame.init()

		self.fps = fps

		self.screen = pygame.display.set_mode((854, 480))
		

		self.event_manager = em.EventManager()

		self.user_event_count = 0

		self.clock = pygame.time.Clock()

		self.scene_manager = scene.SceneManager(self.event_manager)

		self.event_manager.add_callback(pygame.QUIT, self.on_quit)

	def update(self):
		self.event_manager.update()
		
		self.scene_manager.update()

	def late_update(self):
		self.scene_manager.late_update()

	def render(self):
		self.screen.fill((255, 255, 255))
		self.scene_manager.render(self.screen)

		pygame.display.update()
		self.clock.tick(self.fps)
	
	def on_quit(self):
		pygame.quit()
		sys.exit()