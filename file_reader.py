import pdfplumber
import re

PDF_PATH = r"C:\Users\javco\Downloads\EstadoDeCuenta.pdf"
SEARCH_TITLE = "LUGAR"
SEARCH_SUBTITLE = "TOTAL|PRODUCTOS|CARGOS|INFORMACIÓN"

table_data = []

with pdfplumber.open(PDF_PATH) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for t_index in range(len(tables)):
            table_row = tables[t_index][0]
            # Título clave para definir tabla
            if re.search(f"^{SEARCH_TITLE}", str(table_row[0])):
                # Tratar datos
                for data in tables[t_index]:
                    # Omitir subtítulos [tercera columna]
                    # Comienza con dígito y busca subtítulo
                    if re.search(f"^\d.*{SEARCH_SUBTITLE}", data[2]):
                        continue
                    else:
                        table_data.append(data)

print(table_data)
