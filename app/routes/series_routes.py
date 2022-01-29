from flask import Blueprint
from app.controllers.series_controller import create, series, select_by_id
bp = Blueprint("series",__name__)


bp.post("/series")(create)
bp.get("/series")(series)
bp.get("/series/<int:id>")(select_by_id)