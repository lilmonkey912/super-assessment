# Super Data Platform Team – Co-op Case Study

Hi Super 👋

I'm Chloe, and this is my take-home solution for the Data Engineering case. I used Python + pandas to clean and 
transform the dataset into a tidy table. The logic is minimal, readable, and easy to run — just like something I’d 
prototype in the early stages of building an actual data pipeline.

### What I did:
- Cleaned the `Airline Code` column by removing punctuation and random numbers at the start or end (like `12 Air France`)
- Interpolated the missing `FlightCodes` (assumed +10 steps) and cast them to integers
- Split the `To_From` column into `From` and `To`, with proper capitalization
- Left the `DelayTimes` column as-is, since no transformation was specified and it looked like historical data

### How to run it

If you're using macOS and get an error like `ModuleNotFoundError: No module named 'pandas'`, it's probably because 
system Python doesn't have the right packages.

You can run it directly like this:

```bash
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 superpandas.py

Or, better — create a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install pandas
python superpandas.py

That's it!

Thanks for reading — I really enjoyed this one :)

– Chloe


