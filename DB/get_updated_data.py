from .connection import create_connection

def get_dashboard_kpis(consultant_id: int):
    conn = create_connection()
    with conn.cursor() as cur:
        # Horas esta semana
        cur.execute("""
            SELECT COALESCE(SUM(tr.horas_invertidas), 0)
            FROM trabajo_realizado tr
            JOIN asignacion_proyecto ap ON ap.id = tr.asignacion_id
            WHERE ap.consultor_id = %s
              AND tr.fecha >= date_trunc('week', CURRENT_DATE)
              AND tr.fecha <  date_trunc('week', CURRENT_DATE) + INTERVAL '7 days';
        """, (consultant_id,))
        week_hours = cur.fetchone()[0]

        # Horas este mes
        cur.execute("""
            SELECT COALESCE(SUM(tr.horas_invertidas), 0)
            FROM trabajo_realizado tr
            JOIN asignacion_proyecto ap ON ap.id = tr.asignacion_id
            WHERE ap.consultor_id = %s
              AND tr.fecha >= date_trunc('month', CURRENT_DATE)
              AND tr.fecha <  (date_trunc('month', CURRENT_DATE) + INTERVAL '1 month');
        """, (consultant_id,))
        month_hours = cur.fetchone()[0]

        # Proyectos activos
        cur.execute("""
            SELECT COUNT(DISTINCT ap.proyecto_id)
            FROM asignacion_proyecto ap
            WHERE ap.consultor_id = %s AND ap.activo = TRUE;
        """, (consultant_id,))
        active_projects = cur.fetchone()[0]

    return [week_hours, month_hours, active_projects]

if __name__ == "__main__":
    get_dashboard_kpis(1)