import matplotlib.pyplot as plt
line1 = plt.plot([1,2,3,4])
plt.setp(line1, 'color', 'b', 'linewidth', 1.0)
plt.plot([2,3,4,2])
plt.ylabel('Tempo (ms)')
plt.show()
plt.annotate('Item1', xy=(0, 2), xytext=(0, 2.5),
)
plt.savefig('imagem.png')