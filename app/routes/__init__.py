from app.routes.series_routes import bp as bp_post_serie
def init_app(app):
    app.register_blueprint(bp_post_serie)