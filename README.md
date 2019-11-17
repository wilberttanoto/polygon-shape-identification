# Polygon Shape Identification API

An API based on Flask Project.

## Installation

1. Ensure at least python 3.x is installed
2. Ennsure virtualenv is installed to allow different version of library dependency.
```
If you don't have virtualenv installed in your system, you can download it from https://pypi.python.org/pypi/virtualenv.
```
3. Download and extract the code
4. Go to the code folder
5. Type this in the terminal to make virtualenv and install and the requirements
```bash
$ virtualenv flask
$ source flask/bin/activate
$ (flask) $ pip install -r requirements.txt
```
6. To run this application we can make app.py executable: 
```bash
$ chmod a+x app.py
$ ./app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```
7. Use postman or similar application to simulate a "POST" request to http://localhost:5000/api/v1.0/check-shape with this body of JSON
```
{
	"lines": [
		"(1,1), (3,1)",
		"(3,3), (1,3)",
		"(3,3), (1,2)",
		"(1,3), (1,1)",
		"(3,3), (1,1)",
		"(2,1), (4,1)",
		"(4,1), (5,2)",
		"(5,2), (3,3)",
		"(3,1), (3,3)",
		"(1,2), (2,1)"
	]
}
```
8. Check the returned JSON