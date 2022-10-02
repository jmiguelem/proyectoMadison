from flask import Flask

# app instance
app = Flask(__name__)

# EJEMPLO DE COMO SERÍA UNA RPUTE CON MIEMBROS (SOLO EJEMPLO)


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
