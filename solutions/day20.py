from typing import List, Tuple


def read_input(lines: List[str]) -> Tuple[str, List[List[str]]]:
    """
    parse input lines to decode string
    and grid
    """

    i = 0
    decode_string = ""
    while lines[i] not in {"", "\n"}:
        decode_string += lines[i].replace("\n", "")
        i += 1

    i += 1
    grid = []
    while i < len(lines):
        grid.append(list(lines[i].replace("\n", "")))
        i += 1
    return decode_string, grid


def pad_image(img: List[List[str]],
              n: int = 2,
              pad_char: str = ".") -> List[List[str]]:
    """
    pad image with n layers of dark
    cells
    """

    for i, row in enumerate(img):
        padding = [pad_char] * n
        img[i] = padding + row + padding

    padding_row = [pad_char] * len(img[0])
    img = [padding_row] * n + img + [padding_row] * n
    return img


def decode_image(img: List[List[str]],
                 decode_string: str) -> Tuple[List[List[str]], int]:
    """
    decode the image, and return this and the number
    of light '#' cells in the result
    """

    m = [[256, 128, 64], [32, 16, 8], [4, 2, 1]]
    out = []
    total = 0
    for i in range(len(img) - 2):
        row = []
        for j in range(len(img[0]) - 2):
            idx = 0
            for i_0 in range(3):
                for j_0 in range(3):
                    if img[i + i_0][j + j_0] == "#":
                        idx += m[i_0][j_0]

            decoded_pixel = decode_string[idx]
            total += 1 if decoded_pixel == "#" else 0
            row.append(decoded_pixel)
        out.append(row)
    return out, total


def print_img(img: List[List[str]]) -> None:
    """
    print image for debugging purposes
    """

    for line in img:
        print("".join(line))


if __name__ == "__main__":

    from collections import Counter
    with open("inputs/day20.txt") as input_file:
        data = input_file.readlines()

    pad_characters = [".", "#"]
    decoder_string, start_grid = read_input(data)
    # print_img(start_grid)
    # print("---------")
    for i in range(50):
        pad_character = "." if i % 2 == 0 else "#"
        start_grid = pad_image(start_grid, 2, pad_character)
        start_grid, count = decode_image(start_grid, decoder_string)
        # print_img(start_grid)
        # print("-------------")
        print(f"Now {count} cells lit up after {i + 1} iterations")
