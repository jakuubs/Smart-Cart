class Station:
    def __init__(self, collected_plants):
        self.collected_plants = collected_plants  # collected_plants to słownik, przechowuje informacje o oddanych plonach

    def get_all_collected_plants(self):  # zwraca łączną ilość zebranych plonów (suma plonów wszystkich roślin)
        return self.collected_plants["beetroot"] + self.collected_plants["carrot"] + self.collected_plants["potato"] + \
               self.collected_plants["wheat"]

    def get_collected_plants(self, name):  # zwraca łączną ilość oddanych plonów dla podanej rośliny (name)
        return self.collected_plants[name]

    def set_collected_plants(self, name,
                             value):  # dla podanej rośliny (name) ustawia łączną ilość oddanych plonów (value)
        self.collected_plants[name] = value
