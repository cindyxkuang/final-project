from flask_frozen import Freezer
from app import app
import client
freezer = Freezer(app)

INIT_NUM = 200

@freezer.register_generator
def detail():
    for row in client.get_stations(INIT_NUM):
        yield {'row_id': row['id']}
        
@freezer.register_generator
def search(zip_code):
    for row in client.get_by_zip(zip_code):
        yield {'search': zip_code}
if __name__ == '__main__':
    freezer.freeze()