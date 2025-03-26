larg = float(input('A largura da parede: '))
alt = float(input('A altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem dimensão {}x{} e área {}m'.format(larg, alt, area))
print('Você precisará de {}L de tinta para sua parede'.format(tinta))