#!flask/bin/python
from flask import Flask, jsonify, request, abort
from cycle_graph import CycleGraph

app = Flask(__name__)

@app.route('/api/v1.0/check-shape/', methods=['POST'])
def check_shape():
    if not request.json or not 'lines' in request.json:
        abort(400)
    
    shape_type = {
        "3" : "Triangle", #3 edge with 4 vertices
        "4" : "Quadrilateral", #4 edge  with 4 vertices
        "5" : "Pentagon" #5 edge with 5 vertices
    }
    shapes = []

    # modifiy the format into array of array [ ['(1,1)', '(3,1)'], ['(3,3)', '(1,3)'], ]
    line_json = request.json['lines']
    graph = [line.split(", ") for line in line_json]

    # init CyCleGraph Object
    cycle = CycleGraph(graph)
    for cy in cycle.getAllCyclyes():
        shapes.append({
            "name" : shape_type[str(len(cy))],
            "vertices" : cy
        })

    return jsonify({"shapes" : shapes})

if __name__ == '__main__':
    app.run(debug=False)