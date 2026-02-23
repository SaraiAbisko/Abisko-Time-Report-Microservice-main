from flask import Flask

from EndpointData.MT.create.create_asignacion_proyectos_instance import (
    create_asignacion_proyecto_instance
)
from EndpointData.MT.create.create_client_instance import (
    create_client_instance
)
from EndpointData.MT.create.create_consultor_instance import (
    create_consultor_instance
)
from EndpointData.MT.create.create_contact_instance import (
    create_contact_instance
)
from EndpointData.MT.create.create_estado_instance import (
    create_estado_instance
)
from EndpointData.MT.create.create_proyecto_instance import (
    create_proyecto_instance
)
from EndpointData.MT.create.create_servicio_instance import (
    create_servicio_instance
)
from EndpointData.MT.create.create_tipo_cobro_instance import (
    create_tipo_cobro_instance
)
from EndpointData.MT.create.create_trabajo_realizado_instance import (
    create_trabajo_realizado_instance
)

from EndpointData.MT.get.get_tablas_instance import (
    get_asignacion_proyecto_instance,
    get_client_instance,
    get_consultor_instance,
    get_contacto_instance,
    get_estados_instance,
    get_proyecto_instance,
    get_servicio_instance,
    get_tipo_cobro_instance,
    get_trabajo_realizado_instance,
)

from EndpointData.MT.get.get_client_modelo_instance import (
    get_client_modelo_instance
)
from EndpointData.MT.get.get_consultor_modelo_instance import (
    get_consultor_modelo_instance
)
from EndpointData.MT.get.get_proyecto_modelo_instance import (
    get_proyecto_modelo_instance
)
from EndpointData.MT.get.get_registro_horas_modelo_instance import (
    get_registro_horas_modelo_instance
)
from EndpointData.MT.get.get_servicio_modelo_instance import (
    get_servicio_modelo_instance
)


app = Flask(__name__)

@app.get("/hola-mundo")
def hola_mundo():
    return "Hola mundo desde Bruno!"


# POST (create)

@app.post("/crear-asignacion-proyectos")
def create_asignacion_proyecto():
    return create_asignacion_proyecto_instance()

@app.post("/crear-client")
def create_client():
    return create_client_instance()

@app.post("/crear-consultor")
def create_consultor():
    return create_consultor_instance()

@app.post("/crear-contact")
def create_contact():
    return create_contact_instance()

@app.post("/crear-estado")
def create_estado():
    return create_estado_instance()

@app.post("/crear-proyecto")
def create_proyecto():
    return create_proyecto_instance()

@app.post("/crear-servicio")
def create_servicio():
    return create_servicio_instance()

@app.post("/crear-tipo-cobro")
def create_tipo_cobro():
    return create_tipo_cobro_instance()

@app.post("/crear-trabajo-realizado")
def create_trabajo_realizado():
    return create_trabajo_realizado_instance()


# Get (tablas)

@app.get("/obtener-asignacion-proyecto")
def get_asignacion_proyecto():
    return get_asignacion_proyecto_instance()

@app.get("/obtener-client")
def get_client():
    return get_client_instance()

@app.get("/obtener-consultor")
def get_consultor():
    return get_consultor_instance()

@app.get("/obtener-contacto")
def get_contacto():
    return get_contacto_instance()

@app.get("/obtener-estados")
def get_estados():
    return get_estados_instance()

@app.get("/obtener-proyecto")
def get_proyecto():
    return get_proyecto_instance()

@app.get("/obtener-servicio")
def get_servicio():
    return get_servicio_instance()

@app.get("/obtener-tipo-cobro")
def get_tipo_cobro():
    return get_tipo_cobro_instance()

@app.get("/obtener-trabajo-realizado")
def get_trabajo_realizado():
    return get_trabajo_realizado_instance()


# Get Views
@app.get("/obtener-client-modelo")
def get_client_modelo():
    return get_client_modelo_instance()

@app.get("/obtener-consultor-modelo")
def get_consultor_modelo():
    return get_consultor_modelo_instance()

@app.get("/obtener-proyecto-modelo")
def get_proyecto_modelo():
    return get_proyecto_modelo_instance()

@app.get("/obtener-registro-horas-modelo")
def get_registro_horas_modelo():
    return get_registro_horas_modelo_instance()

@app.get("/obtener-servicio-modelo")
def get_servicio_modelo():
    return get_servicio_modelo_instance()


if __name__ == "__main__":
    app.run()
