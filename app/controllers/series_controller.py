from ast import Return
import re
from app.models.series_model import Series
from flask import jsonify, request
from http import HTTPStatus
import psycopg2
from psycopg2.errors import UniqueViolation 


def create():
    try:
        data = request.get_json()
        serie = Series(**data)
        inserted_serie = serie.create_serie()
    
        list_series_keys = ['id','serie', 'seasons','released_date','genre','imdb_rating']
        serie = dict(zip(list_series_keys, inserted_serie))
    
        return serie, HTTPStatus.CREATED
    
    except UniqueViolation:
        return {"error":"This movie already exists on the database"}, HTTPStatus.BAD_REQUEST


def series():
    try:
        list_series_values = Series.get_series()
        list_series_keys = ['id','serie', 'seasons','released_date','genre','imdb_rating']
        list_series = [dict(zip(list_series_keys,  value)) for value in list_series_values]
        return jsonify(list_series), HTTPStatus.OK
    
    except psycopg2.errors.UndefinedTable:
        return jsonify([]), HTTPStatus.OK


def select_by_id(id):
    try:
        serie = Series.get_series_by_id(id)
        list_series_keys = ['id','serie', 'seasons','released_date','genre','imdb_rating']
        serie = dict(zip(list_series_keys, serie))
        return serie, HTTPStatus.OK
    
    except TypeError:
        return {}, HTTPStatus.NOT_FOUND
