import numpy as np
import pandas as pd
import scipy.stats as sc
# import wquntiles
# dictio = {
#    "Alabama": {"population": 4779736, "mud": 5.7, "abbrevation": 'AL'}, "Alasaka": {"population": 710231, "mud": 5.6, "abbrevation": 'AK'}, "Arizona": {"population": 639217, "mud": 4.7, "abbrevation": 'AZ'}, "Arkansas": {"population": 2915918, "mud": 5.6, "abbrevation": 'AR'}, "California": {"population": 37253956, "mud": 4.4, "abbrevation": 'CA'}, "Colorado ": {"population": 529196, "mud": 2.8, "abbrevation": 'CO'}, "Connecticut ": {"population": 357497, "mud": 2.4, "abbrevation": 'CT'}, "Delaware ": {"population": 897934, "mud": 5.8, "abbrevation": 'DE'}}
#
# df = pd.DataFrame(dictio, index=['population', 'mud', 'abbrevation'])
# print(Alabama["population"])
# print(df.to_csv('A:\\am1.csv'))
#
# dictio1 = {"country": ["egypt", "saudi", "nigeria", "sudan"], "population": [
#    100000000, 36000000, 120000000, 70000000], "mud": [5.7, 5.4, 5.2, 4.9], "key": ["ARE", "KSA", "NIG", "SUD"]}
#
# df1 = pd.DataFrame(dictio1, columns=["population"])
# print(df1)
# print(" average= ", end="")
# print(df1.median())

nu = np.identity((4))
print(nu.mean())
print(nu.max())
print(nu.any())
print('*'*20)

# print(dir(np))

state = pd.read_csv('A:\\data.csv')
print(f"mean of mud= {state['mud'].mean()}")
print(f"median of mud= {state['mud'].median()}")
print(f"trim mean of population= {sc.trim_mean(state['population'], 0.1)}")
print(f"median of population= {state['population'].median()}")
print(f"mean of population= {state['population'].mean()}")
print('*'*30)
print(f"av= {np.average(state['mud'], weights=state['population'])}")
print(state['mud'].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))
# print(wquantiles.median(state['mud'], weights=state['population']))
ax = (state['population']/1_000_000).plot.box()
ax.set_ylabel('population (millions)')
