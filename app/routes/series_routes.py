from flask import Blueprint
from app.controllers.series_controller import create, series, select_by_id, creating_table_if_not_exists
from app.models.series_model import Series
bp = Blueprint("series",__name__)

bp.before_request(creating_table_if_not_exists)
bp.post("/series")(create)
bp.get("/series")(series)
bp.get("/series/<int:id>")(select_by_id)