import view
import model
# view.print_field(model.get_field())
def player_turn():
    field = model.get_field()
    view.print_field(field)
    turn = view.enter_player_turn(field)
    model.set_field(turn)
while True:
    player_turn()
