import os
import glob
from dotenv import load_dotenv

import pandas as pd
import pyarrow.parquet as pq

import firebase_admin
from firebase_admin import credentials

from .api import app
from .models.sale import SaleDataModel, db

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = (
    os.environ.get("DATABASE_URL") or "sqlite:///example.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def initialize_database():
    db.create_all()

    data_path = os.environ.get("DATA_PATH")
    parquet_files = glob.glob(f"./{data_path}/*")

    columns_to_filter = [
        "KeyEmployee",
        "KeyProduct",
        "KeyStore",
        "KeyDate",
        "TicketId",
        "Amount",
        "CostAmount",
        "DiscAmount",
    ]
    for file_path in parquet_files:
        print("loading file")
        table = pq.read_table(file_path)
        selected_table = table.select(columns_to_filter)
        df = selected_table.to_pandas()

        df.to_sql(
            SaleDataModel.__tablename__, db.engine, if_exists="append", index=False
        )


with app.app_context():
    print("Initializing DB")
    db.init_app(app)
    initialize_database()
    cred = credentials.Certificate(os.environ.get("FIREBASE_CREDS_URL"))
    firebase_admin.initialize_app(cred)

if __name__ == "__main__":
    app.run(debug=True)
