import random
import copy

# Parameters:
#   See:
#       . Chapter 'Parameter' Python official docs:
#         https://docs.python.org/3/glossary.html
#
#   Type of Parameters:
#       . Positional-or-keyword:
#           def func(foo, bar=None): ...
#           NOTE: specifies an argument that can be passed either positionally or as a keyword argument.
#
#       . Positional-only:
#           def func(posonly1, posonly2, /, positional_or_keyword): ...
#           NOTE: specifies an argument that can be supplied only by position.
#                 Positional-only parameters can be defined by including a / character in the parameter
#                 list of the function definition after them, for example posonly1 and posonly2.
#
#       . Keyword-only:
#           def func(arg, *, kw_only1, kw_only2): ...
#           NOTE: specifies an argument that can be supplied only by keyword.
#                 Keyword-only parameters can be defined by including a single var-positional parameter
#                 or bare * in the parameter list of the function definition before them, for example
#                 kw_only1 and kw_only2.
#
#       . Var-positional:
#           def func(*args, **kwargs): ...
#           NOTE: specifies that an arbitrary sequence of positional arguments can be provided (in addition
#                 to any positional arguments already accepted by other parameters).
#                 Such a parameter can be defined by prepending the parameter name with *, for example args.
#
#       . Var-keyword
#           NOTE: specifies that arbitrarily many keyword arguments can be provided (in addition to any
#                 keyword arguments already accepted by other parameters).
#                 Such a parameter can be defined by prepending the parameter name with **, for example
#                 kwargs in the example above.


class Hat:
    def __init__(self, **kwargs):  # '**kwargs' is the same has '**balls'
        self.contents = []

        for key, value in kwargs.items():
            self.contents += [key] * value
        # 'kwargs'   : key word arguments
        # '**kwargs' : specifies that arbitrarily many keyword arguments can be provided

    def draw(self, draws):
        # Step 1: assure that number of balls to draw are not higher than the number of balls in the hat
        draw_number = min(draws, len(self.contents))

        # Step 2: create a list with the drwa balls
        balls_draw = []

        for num in range(draw_number):
            random_number = random.randint(0, len(self.contents) - 1)
            # Note:
            #   . len(self.contents) - 1 : because we want to obtain the index position of the ball to
            #                              draw, and the index numbers start position, begins at 0.
            ball_draw = self.contents.pop(random_number)
            balls_draw.append(ball_draw)
            # '.pop()' : removes the element at the specified position.
            # 'import ramdom'
            # 'random.random()' : random method. Returns a random number between >0 and <1.
            #                     https://www.w3schools.com/python/ref_random_random.asp
            #                     https://www.freecodecamp.org/news/how-to-use-javascript-math-random-as-a-random-number-generator/
            # Example:
            #   import math
            #   import random
            #   min = 0
            #   maximum = 6
            #   result = math.floor(random.random() * (maximum - min + 1)) + min
            #   print(result)
        return balls_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiment = 0

    for n in range(num_experiments):
        # Step 1: make a copy of the original args, to assure each experiment starts with the original values
        copy_expected_balls = copy.deepcopy(expected_balls)
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        # To assure that each experiment has the same number of balls in the beginning is necessary to
        # make copies of the original 'expected_balls' and 'hat'.
        # See intermediate results:
        print(f'Expected balls: {copy_expected_balls}')
        print(f'Balls drawn from the hat: {balls_drawn}')

        # Step 2: updating the count of balls in 'copy_expected_balls'
        for ball_draw_color in balls_drawn:
            if (ball_draw_color in copy_expected_balls) and (copy_expected_balls[ball_draw_color] > 0):
                copy_expected_balls[ball_draw_color] -= 1
                # See intermediate result:
                print(f'Ball drawn color: {copy_expected_balls}')

        # Step 3: verifying if all values in 'copy_expected_balls' are <= 0, witch means 'successful experiment'
        draw_experiment = sum(copy_expected_balls.values())
        if draw_experiment == 0:
            successful_experiment += 1
        # Notes:
        #   all() function:
        #       . 'all()' : returns True if all items in an iterable are true, otherwise it returns False.
        #                   If the iterable object is empty, the all() function also returns True.
        #       . See: https://www.w3schools.com/python/ref_func_all.asp
        #       . Code using 'all()' function
        #               if all(x <= 0 for x in copy_expected_balls.values()):
        #                   expected_draw += 1

    probability = successful_experiment / num_experiments

    return probability
