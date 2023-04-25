import copy
import random


class Hat:
    # Create the contents that will have the different colours
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    # Takes the num of balls drawn from the hat, without replacing them
    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


# Blah blah
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        drawn_dict = {}
        for ball in drawn_balls:
            if ball in drawn_dict:
                drawn_dict[ball] += 1
            else:
                drawn_dict[ball] = 1
        success = True
        for k, v in expected_balls.items():
            if k not in drawn_dict or drawn_dict[k] < v:
                success = False
                break
        if success:
            count += 1
    return count / num_experiments
