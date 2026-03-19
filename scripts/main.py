import game

def main():
	g = game.Game()
	
	while True:
		g.update()
		g.late_update()
		g.render()

main()