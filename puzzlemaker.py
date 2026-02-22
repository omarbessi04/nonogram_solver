import os
import pytesseract
from PIL import Image


class PuzzleMaker:
    def __init__(self, img_path="hard_data/nonogram1.png", diff="Hard"):
        self.image = Image.open(img_path)
        self.img_width, self.img_height = self.image.size
        self.set_difficulty(diff)

    def set_difficulty(self, diff):
        # if diff == "Medium": 1170 x 2532
        #     self.dims = 10

        #     self.c_left =
        #     self.c_top =
        #     self.c_right =
        #     self.c_bottom =

        #     self.r_left =
        #     self.r_top =
        #     self.r_right =
        #     self.r_bottom =

        #     self.spaces =

        # else:
        self.dims = 15

        self.c_left = self.img_width - 1157
        self.c_top = self.img_height - 1818
        self.c_right = self.c_left + 188
        self.c_bottom = self.c_top + 63

        self.r_left = self.img_width - 251
        self.r_top = self.img_height - 529
        self.r_right = self.r_left + 15
        self.r_bottom = self.r_top + 54

        self.spaces = (17, 16)

    def get_new_puzzle(self):
        self.get_column_images()
        self.get_row_images()

        print("COLUMN")
        for img in os.listdir("column"):
            if img == ".gitignore":
                continue
            print(img, self.read_numbers_from_image(f"column/{img}"))

        print("ROW")
        for img in os.listdir("row"):
            if img == ".gitignore":
                continue
            print(img, self.read_numbers_from_image(f"row/{img}"))

    def get_column_images(self):
        """Saves column numbers into the 'column' folder"""

        for i in range(self.dims):
            cropped_example = self.image.crop(
                (self.c_left, self.c_top, self.c_right, self.c_bottom)
            )
            cropped_example.save(f"column/col_number_{i + 1}.png")

            if i % 2 == 0:
                space_count = self.spaces[0]
            else:
                space_count = self.spaces[1]

            self.c_top += space_count
            self.c_bottom += space_count

    def get_row_images(self):
        """Saves row numbers into the 'row' folder"""

        for i in range(self.dims):
            cropped_example = self.image.crop(
                (self.r_left, self.r_top, self.r_right, self.r_bottom)
            )
            cropped_example.save(f"row/col_number_{i + 1}.png")

            if i % 2 == 0:
                space_count = self.spaces[0]
            else:
                space_count = self.spaces[1]

            self.r_left += space_count
            self.r_right += space_count

    def read_numbers_from_image(self, img_path):
        img = Image.open(img_path)
        img = img.resize((img.width * 2, img.height * 2), Image.NEAREST)
        img = img.convert("L")
        img.save("BIG_IMG.png")

        pytesseract.pytesseract.tesseract_cmd = (
            "C:/Program Files/Tesseract-OCR/tesseract.exe"
        )
        text = pytesseract.image_to_string(img)
        numbers = [int(n) for n in text.split() if n.isdigit()]
        return numbers


a = PuzzleMaker()
a.get_new_puzzle()
