import matplotlib.pyplot as plt

def makesquare(values,sqvalues):
    for n in values:
        sqvalues.append(n**3)

numbers=[n for n in range(1,1001)]
squares=[]
makesquare(numbers,squares)

if __name__ == ('__main__'):
    fig,graph=plt.subplots()
    graph.plot(numbers,squares)
    plt.title("Cubes")
    plt.xlabel('n')
    plt.ylabel('cube of numbers',fontsize=10)
    plt.tick_params(axis='both', labelsize=8)


    plt.show()

