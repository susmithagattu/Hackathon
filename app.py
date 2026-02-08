from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# store expenses in a list
expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = request.form.get("amount")
        category = request.form.get("category")
        note = request.form.get("note")

        expense = {
            "amount": float(amount),
            "category": category,
            "note": note
        }

        expenses.append(expense)
        return redirect("/")

    total = 0
    for e in expenses:
        total += e["amount"]

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)
