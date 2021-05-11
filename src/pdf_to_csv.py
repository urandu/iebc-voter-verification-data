# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("data/raw_data/Building_Bridges_Initiative_File_2.pdf", pages='1-2')[0]
# convert PDF into CSV
tabula.convert_into("data/raw_data/Building_Bridges_Initiative_File_2.pdf", "data/csv_data/Building_Bridges_Initiative_File_2.csv", output_format="csv", pages='1-5')
print(df)