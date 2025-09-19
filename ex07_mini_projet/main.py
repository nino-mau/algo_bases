import json
import pygame


def load_labyrinth(file_path, Labyrinth):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    grid = data["grid"]
    width = len(grid[0])
    height = len(grid)

    start = None
    end = None
    tiles = set()
    points = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                tiles.add((x, y))
            elif cell == "S":
                if start is not None:
                    raise ValueError("Multiple start positions (S) found!")
                start = (x, y)
            elif cell == "E":
                if end is not None:
                    raise ValueError("Multiple end positions (E) found!")
                end = (x, y)
            elif cell == "*":
                points.add((x, y))

    if start is None or end is None:
        raise ValueError("Missing start (S) or end (E) in the labyrinth!")

    return Labyrinth(width, height, start, end, tiles, points)


def render_labyrinth(labyrinth_data, tileSize, screen):
    # Define colors
    WALL_COLOR = (50, 50, 50)
    POINT_COLOR = (255, 215, 0)
    FLOOR_COLOR = (255, 255, 255)
    START_COLOR = (0, 0, 255)
    END_COLOR = (0, 255, 0)

    # Clear screen
    screen.fill(FLOOR_COLOR)

    # Draw tiles
    for x, y in labyrinth_data.tiles:
        pygame.draw.rect(
            screen,
            WALL_COLOR,
            (x * tileSize, y * tileSize, tileSize, tileSize),
        )

    # Draw start positiion
    start_x, start_y = labyrinth_data.start
    pygame.draw.rect(
        screen,
        START_COLOR,
        (start_x * tileSize, start_y * tileSize, tileSize, tileSize),
    )

    # Draw end positiion
    end_x, end_y = labyrinth_data.end
    pygame.draw.rect(
        screen,
        END_COLOR,
        (end_x * tileSize, end_y * tileSize, tileSize, tileSize),
    )

    # Draw points
    for x, y in labyrinth_data.points:
        pygame.draw.rect(
            screen,
            POINT_COLOR,
            (x * tileSize, y * tileSize, tileSize, tileSize),
        )


def render_player(player, tileSize, screen):
    # Define colors
    PLAYER_COLOR = (139, 0, 139)

    # Draw player
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        (player.x * tileSize, player.y * tileSize, tileSize, tileSize),
    )


def draw_victory_screen(screen, labyrinth_data, tileSize):
    screen.fill((0, 0, 0))
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Victory!", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (
        labyrinth_data.width * tileSize // 2,
        labyrinth_data.height * tileSize // 2,
    )
    screen.blit(text, textRect)


def player_action_handler(event, player, game_state, labyrinth_data):
    if event.type == pygame.KEYUP:
        x = player.x
        y = player.y

        # Handle quitting
        if event.key == pygame.K_ESCAPE:
            game_state.is_running = False

        # Handle movement
        match event.key:
            case pygame.K_LEFT:
                if (x - 1, y) not in labyrinth_data.tiles:
                    player.x -= 1
            case pygame.K_RIGHT:
                if (x + 1, y) not in labyrinth_data.tiles:
                    player.x += 1
            case pygame.K_UP:
                if (x, y - 1) not in labyrinth_data.tiles:
                    player.y -= 1
            case pygame.K_DOWN:
                if (x, y + 1) not in labyrinth_data.tiles:
                    player.y += 1

        # Handle victory
        if (x, y) == labyrinth_data.end:
            game_state.is_victory = True


def main():
    LABYRINTH_DATA_PATH = "./ex07_mini_projet/labyrinths/lab-small.json"
    TILE_SIZE = 10

    class Labyrinth:
        def __init__(self, width, height, start, end, tiles, points):
            super(Labyrinth, self).__init__()
            self.width = width
            self.height = height
            self.start = start
            self.end = end
            self.tiles = tiles
            self.points = points

    class Game:
        def __init__(self, is_running, is_victory, is_defeat):
            super(Game, self).__init__()
            self.is_running = is_running
            self.is_victory = is_victory
            self.is_defeat = is_defeat

        def victory(self):
            self.is_running = False
            self.is_victory = True

    class Player:
        def __init__(self, x, y):
            super(Player, self).__init__()
            self.x = x
            self.y = y

    # Create labyrinth instance with data from json
    labyrinth_data = load_labyrinth(LABYRINTH_DATA_PATH, Labyrinth)
    print(labyrinth_data.tiles)

    # Create game instance
    game_state = Game(False, False, False)

    # Initialize pygame environement
    pygame.init()
    pygame.display.set_caption("Labyrinthe")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (labyrinth_data.width * TILE_SIZE, labyrinth_data.height * TILE_SIZE)
    )

    # Create player instance
    player = Player(labyrinth_data.start[0], labyrinth_data.start[1])

    # Game loop
    game_state.is_running = True
    while game_state.is_running:
        # Handle victory
        if game_state.is_victory:
            draw_victory_screen(screen, labyrinth_data, TILE_SIZE)

            # Still handle quitting
            for event in pygame.event.get():
                pygame.event.event_name(event.type)
                if event.key == pygame.K_ESCAPE:
                    game_state.is_running = False
        else:
            # Handle events
            for event in pygame.event.get():
                pygame.event.event_name(event.type)
                if event.type == pygame.QUIT:
                    game_state.is_running = False

                player_action_handler(event, player, game_state, labyrinth_data)

            # Render labyrinth
            render_labyrinth(labyrinth_data, TILE_SIZE, screen)

            # Render player
            render_player(player, TILE_SIZE, screen)

        # Update display
        pygame.display.flip()

        # Set framerate
        clock.tick(60)

    pygame.quit()


main()
