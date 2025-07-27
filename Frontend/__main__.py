from .game import AsteroidsGame


def main() -> None:
    game = AsteroidsGame()
    try:
        game.main_loop()
    finally:
        game.quit_game()


if __name__ == "__main__":
    main()
