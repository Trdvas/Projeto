from flask import Flask, request, jsonify
from models import db, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Rota para criar um produto
@app.route("/produtos", methods=["POST"])
def add_product():
    data = request.get_json()
    name = data.get("name")
    amount = data.get("amount")

    if not name or amount is None:
        return jsonify({"error": "Name and amount are required"}), 400

    new_product = Product(name=name, amount=amount)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added successfully", "product": {"id": new_product.id, "name": name, "amount": amount}}), 201

# Rota para listar os produtos
@app.route("/produtos", methods=["GET"])
def get_products():
    products = Product.query.all()
    result = [{"id": p.id, "name": p.name, "amount": p.amount} for p in products]
    return jsonify(result), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
