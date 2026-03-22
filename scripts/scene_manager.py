import state, scene.intro, scene.title, scene.level, scene.game_over

class SceneManager(state.StateManager):
	def __init__(self, event_manager):
		super().__init__(event_manager)

		intro = scene.intro.Intro(self, event_manager)
		title = scene.title.Title(self, event_manager)
		level = scene.level.Level(self, event_manager)
		pause = scene.level.Pause(self, event_manager)
		game_over = scene.game_over.GameOver(self, event_manager)
		
		self.register_state('Intro', intro)
		self.register_state('Title', title)
		self.register_state('Level', level)
		self.register_state('Pause', pause)
		self.register_state('Game Over', game_over)
		
		self.set_only_current_state('Title')
		