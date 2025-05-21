import pandas as pd
import re
from io import StringIO
# sample data given
data = '''Airline Code;DelayTimes;FlightCodes;To_From
Air Canada (!);[21, 40];20015.0;WAterLoo_NEWYork
<Air France> (12);[];;Montreal_TORONTO
(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa
12. Air France;[78, 66];;Ottawa_VANcouvER
""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal
'''

df = pd.read_csv(StringIO(data), sep=';')

# airline names: remove punctuation and messy numbers like '12'
df['Airline Code'] = df['Airline Code'].apply(
    lambda x: re.sub(r'^\d+\s*|\s*\d+$', '', re.sub(r'[^\w\s]', '', x)).strip()
)

# refill missing flight codes
df['FlightCodes'] = pd.to_numeric(df['FlightCodes'], errors='coerce').interpolate().astype(int)

# split 'To_From' into 'From' and 'To' — and case them respectively
df[['From', 'To']] = df['To_From'].str.title().str.split('_', expand=True)

# DelayTimes kept as-is (e.g. [60, 22, 87]); this seems historical, and no transformation was required
#in real life though, I would confirm with my senior co-workers and make sure the data make sense
print(df[['Airline Code', 'DelayTimes', 'FlightCodes', 'From', 'To']].to_string(index=False))
