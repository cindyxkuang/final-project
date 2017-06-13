from flask_frozen import Freezer
from app import app
import client
freezer = Freezer(app)

INIT_NUM = 200

@freezer.register_generator
def detail():
    for row in client.get_stations(INIT_NUM):
        yield {'row_id': row['id']}

if __name__ == '__main__':
    freezer.freeze()