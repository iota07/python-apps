from turtle import Turtle, Screen
import another_module
from prettytable import PrettyTable

print(another_module.another_variable)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

my_table = PrettyTable()

my_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
my_table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

my_table.align = "l"
print(my_table)
