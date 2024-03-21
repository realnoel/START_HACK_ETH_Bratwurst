import pandas as pd

import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'vercel_app.settings'
application = get_wsgi_application()

from example.models import Fund

df = pd.read_csv('EUESGMANUFACTURER.csv')

unique_valor = df["swissValorNumber"].unique()

unique_categories = df["ESGClassification"].unique()
print(unique_categories)
unique_categories = ['Greenhouse gas emissions', 'Oil', 'Anti-corruption and anti-bribery', 'Animal_Testing', 'Cannabis']

new_df = pd.DataFrame(columns=['Valor', 'ISIN', 'Name', 'Domicile', 'Greenhouse gas emissions', 'Oil', 'Anti-corruption and anti-bribery', 'Animal_Testing', 'Cannabis'])

for valor_id in unique_valor:
    valor_rows = df[df["swissValorNumber"] == valor_id]
    new_entry = {'Valor': valor_id, 'ISIN': valor_rows.iloc[0]["ISIN"], 'Name': valor_rows.iloc[0]["companyLongName"], 'Domicile': valor_rows.iloc[0]["companyDomicile"]}
    for category in unique_categories:
        selected_rows =  valor_rows[valor_rows["ESGClassification"] == category]
        total = 0
        yes = 0
        for _, row in selected_rows.iterrows():
            if isinstance(row["ESGClassSymbol"], str):
                total += 1
                if (row["ESGClassSymbol"][-3:] == "Yes"):
                    yes += 1
        if (total == 0):
            #print(str(valor_id) + " " + category + ": NaN")
            new_entry[category] = "N/A"
        else:
            #print(str(valor_id) + " " + category + ": " + str(yes/total))
            new_entry[category] = yes/total
    
    fund = Fund(valor=new_entry['Valor'], isin=new_entry['ISIN'], name=new_entry['Name'], domicile=new_entry['Domicile'], gge=new_entry['Greenhouse gas emissions'], oil=new_entry['Oil'], acab=new_entry['Anti-corruption and anti-bribery'], animal=new_entry['Animal_Testing'], cannabis=new_entry['Cannabis'])
    fund.save()
    