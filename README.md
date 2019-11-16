# Shape Identification API

Shape Identification API is based on Flask Project.

## Installation

1. Ensure at least python 3.x is installed
2. Ennsure virtualenv is installed to allow different version of library dependency

```bash
$ sudo pip3 install virtualenv
```
3. Download and extract the code
4. Go to the code folder
5. To run this application we have to execute app.py:
```bash
$ chmod a+x app.py
$ ./app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```
6. Use postman to simulate a "POST" request to http://localhost:5000/api/v1.0/check-shape with this body of JSON
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