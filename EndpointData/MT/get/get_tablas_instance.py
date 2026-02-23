from flask import request, jsonify
from DB.objects.asignacion_proyectos import Asignacion_proyecto
from DB.objects.cliente import Client
from DB.objects.consultor import Consultor
from DB.objects.contacto import Contacto
from DB.objects.estado import Estados
from DB.objects.proyecto import Proyecto
from DB.objects.servicio import Servicio
from DB.objects.tipo_cobro import TipoCobro
from DB.objects.trabajo_realizado import Trabajo_realizado


def get_asignacion_proyecto_instance():
    asignaciones = Asignacion_proyecto.get_all()
        
    response = [
        {
            "id": c.id,
            "proyecto_id": c.proyecto_id,
            "consultor_id": c.consultor_id,
            "activo": c.activo
        }
        for c in asignaciones 
    ]

    return jsonify(response), 200


def get_client_instance():
    clientes = Client.get_all()
        
    response = [
        {
            "id": c.id,
            "nombre": c.nombre
        }
        for c in clientes
    ]

    return jsonify(response), 200


def get_consultor_instance():
    consultores = Consultor.get_all()
        
    response = [
        {
            "id": c.id,
            "nombre": c.nombre,
            "coste_hora": c.coste_hora,
            "numero_telefono": c.numero_telefono
        }
        for c in consultores
    ]

    return jsonify(response), 200


def get_contacto_instance():
    contactos = Contacto.get_all()
        
    response = [
        {
            "id": c.id,
            "nombre_contacto": c.nombre_contacto,
            "correo_electronico": c.correo_electronico,
            "numero_telefono": c.numero_telefono,
            "cliente_id": c.cliente_id
        }
        for c in contactos
    ]

    return jsonify(response), 200


def get_estados_instance():
    estados = Estados.get_all()
        
    response = [
        {
            "id": e.id,
            "nombre": e.nombre
        }
        for e in estados
    ]

    return jsonify(response), 200


def get_proyecto_instance():
    proyectos = Proyecto.get_all()
        
    response = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "fecha_inicio": p.fecha_inicio,
            "fecha_fin": p.fecha_fin,
            "costo": p.costo,
            "descripcion": p.descripcion,
            "cliente_id": p.cliente_id,
            "servicio_id": p.servicio_id,
            "proyecto_estado": p.proyecto_estado,
            "imputable": p.imputable
        }
        for p in proyectos
    ]

    return jsonify(response), 200


def get_servicio_instance():
    servicios = Servicio.get_all()
        
    response = [
        {
            "id": s.id,
            "nombre_servicio": s.nombre_servicio,
            "descripcion_servicio": s.descripcion_servicio,
            "tipo_cobro_id": s.tipo_cobro_id
        }
        for s in servicios
    ]

    return jsonify(response), 200


def get_tipo_cobro_instance():
    tipos = TipoCobro.get_all()
        
    response = [
        {
            "id": t.id,
            "tipo_cobro": t.tipo_cobro,
            "horas_relacionadas": t.horas_relacionadas
        }
        for t in tipos
    ]

    return jsonify(response), 200


def get_trabajo_realizado_instance():
    trabajos = Trabajo_realizado.get_all()
        
    response = [
        {
            "id": tr.id,
            "nombre_actividad": tr.nombre_actividad,
            "horas_invertidas": tr.horas_invertidas,
            "hora_extra": tr.hora_extra,
            "asignacion_id": tr.asignacion_id,
            "fecha": tr.fecha
        }
        for tr in trabajos
    ]

    return jsonify(response), 200
