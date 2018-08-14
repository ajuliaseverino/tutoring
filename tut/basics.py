# print('Hello world')
# x = 5.6
# print(x)
#
# print("\nFor loop from 0 to 9.")
# for i in range(10):
#     print(i)


def input_switch():
    """A function definition.
    Calling the function by typing input_switch() will run this code.
    The code does *not* get run when you create the function.
    """
    user_input = input("type some stuff ")
    print("you typed {}".format(user_input))

    if user_input == "yes":
        print("ok, good")
    elif user_input == "no":
        print("ok, bad")
    else:
        print("khsdf")


# print("\nFunctions with arguments now.")


def pos_neg(some_data_asdf):
    """Arguments (some_data_asdf) are used when there's some data you don't know in advance, but you *do* know
    what you want to do with that data.

    """
    if some_data_asdf < 0:
        return some_data_asdf - 2
    else:
        return some_data_asdf + 2


# Runs the identity function, but with all the 'some_data_asdf' replaced by 5.
# identity(-5)
# identity(5)
# identity(6)


# print("\nVery very simple calculator now.")


def simple_calculator(right_hand_side, operator, left_hand_side):
    if operator == "+":
        return right_hand_side + left_hand_side
    elif operator == "-":
        return right_hand_side - left_hand_side
    elif operator == "*":
        return right_hand_side * left_hand_side
    elif operator == "/":
        return right_hand_side / left_hand_side





