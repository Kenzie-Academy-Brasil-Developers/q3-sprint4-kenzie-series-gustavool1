from app.models import DatabaseConnector
from datetime import datetime 
class Series(DatabaseConnector):
    def __init__(self, serie, seasons, genre, imdb_rating) -> None:
        self.serie = serie.title()
        self.seasons = seasons
        self.released_date = self.setting_releasing_date()
        self.genre = genre.title()
        self.imbd_rating = imdb_rating

    
    @classmethod
    def get_series(cls):
        cls.get_conn_cur()
        query = """
            CREATE TABLE IF NOT EXISTS ka_series(
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL 
            );
            SELECT * FROM ka_series;
        """
        cls.cur.execute(query)
    
        series_list = cls.cur.fetchall()
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()
        return series_list


    @classmethod
    def get_series_by_id(cls, id):
        cls.get_conn_cur()
        query = """ 
            CREATE TABLE IF NOT EXISTS ka_series(
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL 
                );
            SELECT * FROM ka_series WHERE id= %s 
        """
        print(query)
        cls.cur.execute(query, [id])
        serie = cls.cur.fetchone()

        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()
        return serie

    @classmethod
    def serialize_serie(cls, data):
        list_series_keys = ['id','serie', 'seasons','released_date','genre','imdb_rating']
        if type(data) is list:
            return [dict(zip(list_series_keys,  value)) for value in data]
        if type(data) is dict:
            return dict(zip(list_series_keys, data))

    def create_serie(self):
        self.get_conn_cur()

        query = """
            CREATE TABLE IF NOT EXISTS ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL 
            );
            INSERT INTO ka_series  
	            (serie, seasons,released_date,genre,imdb_rating)
            VALUES
	            (%s, %s,%s,%s,%s)
            RETURNING *
        """
        values_list = list(self.__dict__.values())

        self.cur.execute(query,values_list)
        inserted_serie = self.cur.fetchone()

        self.conn.commit()
        self.cur.close()
        self.conn.close()

        return inserted_serie
        

    def setting_releasing_date(self):
        return str(datetime.now().strftime("%d/%m/%Y %H:%M")) 