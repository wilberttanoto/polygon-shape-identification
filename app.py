#!flask/bin/python
from flask import Flask, jsonify, request, abort
from cycle_graph import CycleGraph

app = Flask(__name__)

@app.route('/api/v1.0/check-shape/', methods=['POST'])
def polygonShape():
    # simple validation for the body JSON 
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
        vertices = []
        # connecting each cycle..
        for i,_ in enumerate(cy):
            # need to check length of array less than 2, cos edge = 2 node points
            if (len(cy[i:i+2]) < 2):
                v = [cy[i]] + [cy[0]]
            else:
                v = cy[i:i+2]
            vertices.append(v)    

        shapes.append({
            "name" : shape_type[str(len(cy))],
            "vertices" : vertices
        })

    return jsonify(shapes=shapes)

if __name__ == '__main__':
    app.run(debug=False)