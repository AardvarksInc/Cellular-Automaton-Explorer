from engine import *

import pygame
import time

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cellula Automaton Explorer")
colours = [FRBLACK, FRWHITE]
font = pygame.font.Font(None, 20)


def rule_display_64(bits: list) -> str:
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&"
    base64 = ""

    bits_str = "".join(str(bit) for bit in bits)
    num = int(bits_str, 2)

    while num > 0:
        num, i = divmod(num, 64)
        base64 = chars[i] + base64
    while len(base64) < 8:
        base64 = chars[0] + base64
    return base64


def input_binary(rule_string: str):
    while len(rule_string) <= 511:
        rule_string = "0" + rule_string
    return rule_string


def input_base_64(rule_string: str):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@&"
    binary = ""
    for char in rule_string:
        current_binary = format(chars.index(char), "06b")
        binary += current_binary
    print(input_binary(binary))
    return input_binary(binary)


def rule_array_to_decimal(rule_array: list[int]) -> int:
    binary_str = "".join(str(bit) for bit in rule_array)
    decimal_number = int(binary_str, 2)

    return decimal_number


def decimal_to_rule_array(decimal_number: int) -> list[int]:
    binary_str = format(decimal_number, "0512b")
    rule_array = [int(bit) for bit in binary_str]

    return rule_array


def draw_grid(cell_group):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * SQUARE_SIZE,
                row * SQUARE_SIZE + MENUBAR_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            )
            pygame.draw.rect(WIN, colours[cell_group.cells[row][col].state], rect)


def main():
    counter = 0
    move_size = 1
    rule = RULE  # [1 for i in range(2**9)]
    cell_group = Grid(GRID_SIZE, rule, True)

    clock = pygame.time.Clock()
    run = True
    cycle = False
    while run:
        clock.tick(FRAME_RATE)
        if cycle:
            if counter >= 120:
                next_rule = rule_array_to_decimal(cell_group.rule) + 1
                cell_group = Grid(GRID_SIZE, decimal_to_rule_array(next_rule), True)
                counter = 0
            counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    rule = [min(1, rd.randint(0, 4)) for i in range(2**9)]
                    cell_group = Grid(GRID_SIZE, rule, True)
                elif event.key == pygame.K_r:
                    cell_group.reset()
                elif event.key == pygame.K_LEFT:
                    next_rule = max(rule_array_to_decimal(cell_group.rule) - 1, 0)
                    cell_group.rule = decimal_to_rule_array(next_rule)
                elif event.key == pygame.K_RIGHT:
                    next_rule = rule_array_to_decimal(cell_group.rule) + 1
                    cell_group.rule = decimal_to_rule_array(next_rule)
                elif event.key == pygame.K_UP:
                    next_rule = max(
                        rule_array_to_decimal(cell_group.rule) - move_size, 0
                    )
                    cell_group.rule = decimal_to_rule_array(next_rule)
                elif event.key == pygame.K_DOWN:
                    next_rule = rule_array_to_decimal(cell_group.rule) + move_size
                    cell_group.rule = decimal_to_rule_array(next_rule)
                elif event.key == pygame.K_1:
                    move_size *= 2
                    print(move_size)
                elif event.key == pygame.K_2:
                    move_size = max(move_size // 2, 1)
                    print(move_size)
                elif event.key == pygame.K_s:
                    with open("rules.evl", "a") as file:
                        for rule_bit in cell_group.rule:
                            file.write(str(rule_bit))
                        file.write("\n")
                elif event.key == pygame.K_l:
                    saved_rules = []
                    print("select a rule from below: ")
                    with open("rules.evl", "r") as file:
                        for line in file:
                            saved_rules.append(line)
                    for x, i in enumerate(saved_rules):
                        print(f"{x}. {i}")
                    cell_group.rule = [
                        int(c) for c in saved_rules[int(input("[>]: "))].strip()
                    ]
                elif event.key == pygame.K_e:
                    new_rule_type = input(
                        "please enter a rule in either base-64 (s) or in binary (b): "
                    )

                    new_rule = ""
                    if new_rule_type == "s":
                        new_rule = input_base_64(input("please enter the rule: "))

                    elif new_rule_type == "b":
                        new_rule = input_binary(input("please enter the rule: "))
                    cell_group.rule = [int(bit) for bit in new_rule]
                elif event.key == pygame.K_c:
                    cycle = not cycle

        WIN.fill(BLACK)
        cell_group.update()
        text = font.render(f"{rule_display_64(cell_group.rule)}", True, WHITE, BLACK)
        pygame.draw.rect(
            WIN,
            (200, 200, 200),
            pygame.Rect(0, 0, WIDTH, MENUBAR_SIZE),
        )
        draw_grid(cell_group)
        WIN.blit(text, (10, MENUBAR_SIZE // 2))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
