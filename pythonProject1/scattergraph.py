import matplotlib.pyplot as plt
from linegraph import numbers, squares



plt.style.use('seaborn-v0_8-whitegrid')
fig, ax=plt.subplots()
ax.scatter(numbers,squares,c=squares,cmap=plt.cm.Greens,s=10)
ax.set_title("Square Numbers", fontsize=11)
ax.set_xlabel('Value', fontsize=11)
ax.set_ylabel('Square Value', fontsize=11)
ax.tick_params(axis='both', labelsize=8)


plt.savefig('squares_plot.png',dpi=600,bbox_inches='tight')
plt.show()