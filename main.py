from flask import Flask, render_template

app=Flask(__name__)

theader=("Name", "Age", "Years of Experience", "Salary")

data=(("Albert", "31", "10", "$10000.00"),
      ("Bob", "40", "5", "$10000.00"),
      ("Smith", "26", "4", "$5000.00"),
      ("John", "56", "30", "$8000.00"),
      ("Sam", "24", "2", "$40000.00"),
      ("Nick", "30", "8", "$7000.00"),
      ("Katy", "39", "10", "$11000.00")
      )

@app.route('/')

def table():
   return render_template("table.html", theader=theader, data=data)

if __name__== "__main__":
     app.run(debug=True)


