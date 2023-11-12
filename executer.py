from oop.game import start_game, GAMEOVER

#import oop.dataloader as dt

from oop.dataloader import DataLoader

start_game()
d = DataLoader(path="path", isdirectory=False)
d.printme()
