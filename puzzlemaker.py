import pytesseract
from PIL import Image


class PuzzleMaker:
    def __init__(self, img_path="data/nonogram1.png"):
        self.image = Image.open(img_path)
        self.img_width, self.img_height = self.image.size

    def get_new_puzzle(self):
        self.get_column_images()
        self.get_row_images()
        print(self.read_numbers_from_image("column/col_number_2.png"))

    def get_column_images(self):
        """Saves column numbers into the 'column' folder"""

        left = 3
        top = self.img_height - 474
        right = 52
        bottom = top + 17

        for i in range(15):
            cropped_example = self.image.crop((left, top, right, bottom))
            cropped_example.save(f"column/col_number_{i + 1}.png")

            if i % 2 == 0:
                TOP_BOT_DIFF = 17
            else:
                TOP_BOT_DIFF = 16
            top += TOP_BOT_DIFF
            bottom += TOP_BOT_DIFF

    def get_row_images(self):
        """Saves row numbers into the 'row' folder"""

        left = self.img_width - 251
        top = self.img_height - 529
        right = left + 15
        bottom = top + 54

        for i in range(15):
            cropped_example = self.image.crop((left, top, right, bottom))
            cropped_example.save(f"row/col_number_{i + 1}.png")

            if i % 2 == 0:
                TOP_BOT_DIFF = 17
            else:
                TOP_BOT_DIFF = 16

            left += TOP_BOT_DIFF
            right += TOP_BOT_DIFF

    def read_numbers_from_image(img_path):
        img = Image.open(img_path)
        img = img.resize((img.width * 4, img.height * 4), Image.NEAREST)
        img = img.convert("L")

        text = pytesseract.image_to_string(img, config="--psm 6 digits")
        numbers = [int(n) for n in text.split() if n.isdigit()]
        return numbers


a = PuzzleMaker()
a.get_new_puzzle()
