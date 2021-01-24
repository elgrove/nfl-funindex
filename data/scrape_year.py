from gridiron_scraper.scraper import updateDB, updateDB_year
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

year = input('Enter the year to scrape:')

updateDB_year(cursor, year)
'Scraping complete'
conn.commit()
'Data update committed'
