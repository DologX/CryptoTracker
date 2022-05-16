# crypto display
import requests

# Get MEX Price
mex_info = requests.get('https://api.elrond.com/tokens/MEX-455c57').json()
mex_price = mex_info["price"]

# Display MEX Price
print("MEX Value: " + str(mex_price)[:8] + "$")
