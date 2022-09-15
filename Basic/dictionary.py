def dictionary_comprehension(letter):
    planets = {'one': 'Mercury',
               'two': 'Venus',
               'three': 'Earth',
               'four': 'Mars',
               'five': 'Jupiter',
               'six': 'Saturn',
               'seven': 'Uranus',
               'eighth': 'Neptune'}
    planetsFiltered = {key: value for (key, value) in planets.items() if letter in value}
    print(planetsFiltered)


dictionary_comprehension("e")
