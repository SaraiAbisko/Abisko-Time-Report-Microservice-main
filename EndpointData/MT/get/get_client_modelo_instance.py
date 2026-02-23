from flask import request, jsonify
from DB.objects.cliente_modelo import ClientModelo

def get_client_modelo_instance():
    cliente_id = request.args.get("cliente_id", type=int)

    if "cliente_id" in request.args and cliente_id is None:
        return jsonify({"error": "'cliente_id' must be an integer"}), 400

    if cliente_id:
        clientes = ClientModelo.get_clientes(cliente_id)
    else:
        clientes = ClientModelo.get_all_clientes()
        
    response = [
        {
            "id_cliente": c.id_cliente,
            "nombre_empresa": c.nombre_empresa,
            "contacto_principal": c.contacto_principal,
            "correo_contacto": c.correo_contacto,
            "telefono_contacto": c.telefono_contacto
        }
        for c in clientes
    ]

    return jsonify(response), 200
