import game

def main():
	g = game.Game(20)
	
	while True:
		g.update()
		g.late_update()
		g.render()

main()