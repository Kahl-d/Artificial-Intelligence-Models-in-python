from flask import Flask, jsonify
from ucs import ucs



app = Flask(__name__)



class grid_city:
    def __init__(self, x, y):
        self.x_max = x
        self.y_max = y

    class State:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    def start_state(self):
        return self.State(0, 0)

    def end_state(self):
        return self.State(self.x_max, self.y_max)

    def actions(self, state):
        possible_actions = []

        possible_actions.append((0, 1))
        possible_actions.append((0, - 1))
        possible_actions.append((1, 0))
        possible_actions.append((- 1, 0))

        return possible_actions

    def cost(self, state):
        # print(1 + max(state.x, 0))
        cost = 1 + max(state.x, 0)
        return cost


    def Succ(self, state, a):
        # print(state.x + a[0],',', state.y + a[1])
        return self.State(state.x + a[0], state.y + a[1])


    def isEnd(self,state):
        if state == self.end_state():
            return True





@app.route('/main')
def main():
    obj = grid_city(3,2)
    start = obj.start_state()
    end = obj.end_state()

    # print(obj.actions(start))

    path, visited = ucs(obj, start, end)

    path_list = list(path)
    visited_list = list(visited)

    ret = {
        'path': path_list,
        'visited': visited_list
    }

    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True)