from flask import request, jsonify
from DB.objects.registro_horas_modelo import RegistroHorasModelo

def get_registro_horas_modelo_instance():
    id_registro = request.args.get("id_registro", type=int)

    if "id_registro" in request.args and id_registro is None:
        return jsonify({"error": "'id_registro' must be an integer"}), 400

    if id_registro:
        registros = RegistroHorasModelo.get_registros(id_registro)
    else:
        registros = RegistroHorasModelo.get_all_registros()
        
        
    response = [
        {
            "id_registro": c.id_registro,
            "fecha_registro": c.fecha_registro,
            "total_horas": c.total_horas,
            "resumen_trabajo_realizado": c.resumen_trabajo_realizado,
            "etapa_proyecto": c.etapa_proyecto,
            "iniciativa_cliente": c.iniciativa_cliente,
            "id_consultor": c.id_consultor,
            "id_proyecto": c.id_proyecto,
            "id_servicio": c.id_servicio
        }
        for c in registros
    ]
    
    return jsonify(response), 200