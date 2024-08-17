import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Carregar dados das reações a partir do arquivo reactions.json
def load_reactions():
    try:
        with open('reactions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Salvar dados das reações no arquivo reactions.json
def save_reactions(reactions_data):
    with open('reactions.json', 'w') as f:
        json.dump(reactions_data, f, indent=4)

dangerous_animals = [
    {"name": "Brown Snake", "defense": "Stay still and avoid eye contact.", "food_chain": "Pequenos mamíferos -> Cobras maiores", "animal_pic": "brown_snake.jpg"},
    {"name": "Blue Bottle Jellyfish", "defense": "Be cautious when visiting Australian beaches, especially during the warmer months, and pay attention to warning signs. Wear protective clothing and vinegar can be used to treat stings. Seek medical help for severe reactions.", "food_chain": "Zooplankton -> Small Fish -> Blue Bottle Jellyfish", "animal_pic": "blue_jellyfish.jpg", "sound_link": ""},
    {"name": "Saltwater Crocodile", "defense": "Avoid areas known to be crocodile habitats. Keep a distance from water where these crocodiles might be present.", "food_chain": "Small Fish -> Larger Fish -> Saltwater Crocodile", "animal_pic": "saltwater_crocodile.jpg", "sound_link": "https://cdn.discordapp.com/attachments/1134994014928650291/1146870699911299162/saltwater_crocodile_sound_effects_320_kbps.mp3"},
    {"name": "Coastal Taipan", "defense": "Avoid handling or provoking these snakes if encountered. Stay on marked paths when hiking and wear protective clothing and footwear. Seek immediate medical attention if bitten.", "food_chain": "Small Mammals -> Birds -> Coastal Taipan", "animal_pic": "coastal_taipan.jpg", "sound_link": ""},
    {"name": "Dingo", "defense": "Stay calm, don't turn your back, and make yourself appear larger.", "food_chain": "Prey (small mammals, rodents, birds, reptiles) -> Dingos -> Predators (large birds of prey, crocodiles)", "animal_pic": "dingo.jpg", "sound_link": "https://cdn.discordapp.com/attachments/1134994014928650291/1146870692898406530/Dingo_howling_in_Queensland._Wild_dog_of_Australia_320_kbps.mp3"},
    {"name": "Cone Snail", "defense": "Avoid picking up shells on Australian beaches, as cone snails can often hide within them. Do not handle or provoke these snails, as their venomous stings can be extremely dangerous. Seek medical attention if stung.", "food_chain": "Small Fish -> Other Snails -> Cone Snail", "animal_pic": "cone_snail.jpg", "sound_link": ""}
    # Adicione mais animais aqui
]

animal_cases = [
    {"title": "Girl at risk in Australia after encountering deadly bird", "description": "Melania found the bird that is one of Australia's most famous and iconic animals. This happened within just a week of her being in the country. She went there to work on Working Holiday, a special visa for young people between 18 and 30 years old."},
    {"title": "51-year-old man escaped being bitten on the head by the animal", "description": "A 51-year-old Australian man escaped with his life after being attacked by a saltwater crocodile on Saturday. Alongside his wife and friends, Marcus McGowan was diving at a resort in Queensland, Australia, when he was surprised by the animal."},
    {"title": "Woman is bitten by one of the world's most venomous octopuses in Australia", "description": "A 30-year-old Australian woman was attacked by a Hapalochlaena lunulata, a species of octopus popularly known as the blue-ringed octopus. The case occurred on Thursday (16) at Chinamans Beach, Sydney, Australia. This type of octopus is known to be able to incapacitate up to 20 adult men."},
    {"title": "Diver attacked by a shark in Australia.", "description": "In January 2021, a diver was attacked by a great white shark in Esperance Bay, Western Australia. The diver survived the attack but suffered serious injuries to his legs."},
    {"title": "Gardener bitten by a funnel-web spider in Australia", "description": "In September 2020, a man was bitten by a funnel-web spider while working in his garden in Sydney. The bite caused severe pain and swelling, and the man required medical treatment."},
    {"title": "Gardener attacked by a brown snake in Australia", "description": "In 2017, a man was bitten by a brown snake while working in his garden in South Australia. He was taken to the hospital and treated with antivenom to neutralize the venom."}

]


@app.route('/')
def index():
    return render_template('index.html', dangerous_animals=dangerous_animals)

@app.route('/animal/<int:animal_id>', methods=['GET', 'POST'])
def animal(animal_id):
    animal = dangerous_animals[animal_id]

    reactions_data = load_reactions()

    if request.method == 'POST':
        reaction_type = request.form.get('reaction_type')
        if reaction_type in ['scared', 'heart', 'laugh']:
            reactions_data.setdefault(str(animal_id), {}).setdefault(reaction_type, 0)
            reactions_data[str(animal_id)][reaction_type] += 1
            save_reactions(reactions_data)

    return render_template('animal.html', animal=animal, animal_id=animal_id, reactions=reactions_data.get(str(animal_id), {}))

@app.route('/cases')
def cases():
    return render_template('cases.html', animal_cases=animal_cases)

@app.route('/fonts')
def fonts():
    return render_template('fonts.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
