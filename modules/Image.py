import pygame


image_paths = {
    # Each tile image has a size of 89x89 pixels.
    "covered": "images/png/covered.png",
    "flag": "images/png/flag.png",
    "flag_wrong": "images/png/flag_wrong.png",
    "mine": "images/png/mine.png",
    "mine_red": "images/png/mine_red.png",
    "0": "images/png/0.png",
    "1": "images/png/1.png",
    "2": "images/png/2.png",
    "3": "images/png/3.png",
    "4": "images/png/4.png",
    "5": "images/png/5.png",
    "6": "images/png/6.png",
    "7": "images/png/7.png",
    "8": "images/png/8.png",
}


class Image:
    tile_size = 89    
    
    def load_image(path):
        image = pygame.image.load(path)
        scaled_image = pygame.transform.scale(image, (Image.tile_size, Image.tile_size))
        return scaled_image
    
    def covered():
        return Image.load_image(image_paths["covered"])
    
    def flag():
        return Image.load_image(image_paths["flag"])
    
    def flag_wrong():
        return Image.load_image(image_paths["flag_wrong"])
    
    def mine():
        return Image.load_image(image_paths["mine"])
    
    def mine_red():
        return Image.load_image(image_paths["mine_red"])
    
    def number(number: int):
        return Image.load_image(image_paths[str(number)])


if __name__ == "__main__":
    print(type(Image.covered()))

