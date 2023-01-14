import sqlite3
import pandas as pd

conn = sqlite3.connect('app/db/telzir', check_same_thread=False)

cursor_obj = conn.cursor()
