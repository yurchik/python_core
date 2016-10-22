from collections import Counter

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus nobis ex rem magni, et. Nemo odit cupiditate'\
       ', dicta quis, officia quibusdam exercitationem in labore ab tempora eaque dolore rerum incidunt corrupti '\
       'placeat soluta ipsum? Sunt libero quam quia ratione rem, vel fuga deserunt repudiandae explicabo '\
       'ex, adipisci dolore corporis velit, accusamus quaerat quibusdam mollitia. Temporibus natus minima, '\
       'minus, dolor facilis in maiores porro. Sunt sapiente porro, quas possimus esse iusto, autem dolore! '\
       'Natus eius eligendi quidem ea itaque officiis impedit fugit repellendus, velit quisquam sed eos. Molestias '\
       'voluptatum unde praesentium quasi cupiditate ipsum provident saepe, accusamus sed, doloribus mollitia eius.'

words = text.split()

counter = Counter(words)
common = counter.most_common(3)

print(common)