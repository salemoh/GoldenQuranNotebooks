import sqlite3

# Open connection to dest DB
dest_conn = sqlite3.connect("Qaloon_new_1260.db")
dest_cur = dest_conn.cursor()

# Get all rows in ayahinfo_1260.db
conn = sqlite3.connect("ayahinfo_1260.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
QUERY = 'select * from glyphs'
cur.execute(QUERY)

# Loop over rows and insert into new table
for row in cur:
    new_id = row['glyph_id']

    x = int(row['min_x'])
    y = int(row['min_y'])

    upper_left_x = x
    upper_left_y = y

    lower_right_x = int(row['max_x'])
    lower_right_y = int(row['max_y'])

    width = lower_right_x - upper_left_x
    height = lower_right_y - upper_left_y

    upper_right_x = lower_right_x
    upper_right_y = upper_left_y

    lower_left_x = upper_left_x
    lower_left_y = lower_right_y

    ayah = row['ayah_number']
    surah = row['sura_number']
    page_number = row['page_number']
    line = row['line_number']

    ayah_text = 'id={new_id}, x={x}, y={y}, upper_left_x={upper_left_x}, upper_left_y={upper_left_y}, lower_right_x={lower_right_x}, lower_right_y={lower_right_y}, width={width}, height={height}, upper_right_x={upper_right_x}, upper_right_y={upper_right_y}, lower_left_x={lower_left_x}, lower_left_y={lower_left_y}, ayah={ayah}, surah={surah}, page_number={page_number}, line={line}'
    ayah_text_formatted = ayah_text.format(new_id = new_id, x = x, y = y, upper_left_x = upper_left_x, upper_left_y = upper_left_y, lower_right_x = lower_right_x, lower_right_y = lower_right_y, width = width, height = height, upper_right_x = upper_right_x, upper_right_y = upper_right_y, lower_left_x = lower_left_x, lower_left_y = lower_left_y, ayah = ayah, surah = surah, page_number = page_number, line = line)
    print(ayah_text_formatted)

    # Insert into new table
    insert_tuple = (x, y, width, height, upper_left_x, upper_left_y, upper_right_x, upper_right_y, lower_right_x, lower_right_y, lower_left_x, lower_left_y, ayah, line, surah, page_number, new_id)
    print('insert_tuple = {insert_tuple}'.format(insert_tuple = insert_tuple))
    dest_cur.execute('insert into page values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', insert_tuple)
    dest_conn.commit()