from flask import request, jsonify
from DB.objects.proyecto_modelo import ProyectoModelo

def get_proyecto_modelo_instance():
    id_proyecto = request.args.get("id_proyecto", type=int)

    if "id_proyecto" in request.args and id_proyecto is None:
        return jsonify({"error": "'id_proyecto' must be an integer"}), 400

    if id_proyecto:
        proyectos = ProyectoModelo.get_proyectos(id_proyecto)
    else:
        proyectos = ProyectoModelo.get_all_proyectos()
        
        
    response = [
        {
            "id_proyecto": c.id_proyecto,
            "nombre_proyecto": c.nombre_proyecto,
            "cliente_id_cliente": c.cliente_id_cliente,
            "fecha_inicio": c.fecha_inicio,
            "fecha_fin": c.fecha_fin,
            "descripcion": c.descripcion,
            "estado": c.estado
        }
        for c in proyectos
    ]
    
    return jsonify(response), 200
