from django.core.management.base import BaseCommand
from game.models import Destination

data =[
    {
        "city": "Berlin",
        "country": "Germany",
        "clues": [
            "Once divided by a wall that symbolized the Cold War.",
            "Home to the Brandenburg Gate, a historical landmark."
        ],
        "fun_fact": [
            "Berlin has more bridges than Venice—around 1,700!",
            "Currywurst, a popular German snack, was invented in Berlin."
        ],
        "trivia": [
            "The Berlin Wall fell in 1989, leading to the reunification of Germany.",
            "Berlin is the largest city in Germany by both population and area."
        ]
    },
    {
        "city": "Dubai",
        "country": "United Arab Emirates",
        "clues": [
            "This city is home to the tallest building in the world.",
            "Famous for its artificial islands shaped like palm trees."
        ],
        "fun_fact": [
            "Dubai's Burj Khalifa stands at 828 meters, making it the tallest skyscraper.",
            "Dubai has an indoor ski resort inside a shopping mall!"
        ],
        "trivia": [
            "Gold ATMs in Dubai allow people to withdraw real gold bars.",
            "The city hosts the world's largest shopping mall, the Dubai Mall."
        ]
    },
    {
        "city": "Toronto",
        "country": "Canada",
        "clues": [
            "This city has one of the tallest free-standing towers in the world.",
            "Known for its multicultural diversity and hockey culture."
        ],
        "fun_fact": [
            "Toronto has over 10 million trees, making it one of the greenest cities.",
            "The CN Tower was the tallest structure in the world until 2009."
        ],
        "trivia": [
            "Toronto’s PATH is the largest underground shopping complex in the world.",
            "The city is home to the Toronto Raptors, the first Canadian NBA team."
        ]
    },
    {
        "city": "Cape Town",
        "country": "South Africa",
        "clues": [
            "A city with a famous flat-topped mountain.",
            "Known for its stunning beaches and wine regions."
        ],
        "fun_fact": [
            "Cape Town was the first European settlement in South Africa.",
            "The city’s Table Mountain is one of the New 7 Wonders of Nature."
        ],
        "trivia": [
            "Cape Town has a colony of African penguins at Boulders Beach.",
            "It was the first city outside Europe to get Blue Flag status for its beaches."
        ]
    },
    {
        "city": "Moscow",
        "country": "Russia",
        "clues": [
            "Home to a colorful cathedral with onion-shaped domes.",
            "Known for the Red Square and the Kremlin."
        ],
        "fun_fact": [
            "Moscow’s metro system is one of the most beautiful in the world, with chandeliers and art.",
            "The city experiences extreme temperature shifts, from -30°C in winter to 30°C in summer!"
        ],
        "trivia": [
            "The Kremlin has a secret subway system used by government officials.",
            "Moscow is the largest city in Europe by population."
        ]
    },
    {
        "city": "Seoul",
        "country": "South Korea",
        "clues": [
            "This city is a major tech hub and home to K-pop culture.",
            "Features a historic palace in the heart of a modern metropolis."
        ],
        "fun_fact": [
            "Seoul’s Lotte World is the world’s largest indoor theme park.",
            "The city has the fastest internet speeds in the world!"
        ],
        "trivia": [
            "Seoul has more than 25 districts, each with its own unique vibe.",
            "The city’s subway system is one of the most efficient and cleanest in the world."
        ]
    },
    {
        "city": "Mexico City",
        "country": "Mexico",
        "clues": [
            "Built on top of an ancient Aztec capital.",
            "Sinks about 50 cm per year due to its foundation on a lakebed."
        ],
        "fun_fact": [
            "Mexico City has over 150 museums, making it one of the top cities for culture.",
            "It has the largest plaza in Latin America, the Zócalo."
        ],
        "trivia": [
            "Tacos al pastor, a popular Mexican dish, originated in Mexico City.",
            "The city has the second-highest number of palaces in the world after Paris."
        ]
    },
    {
        "city": "Singapore",
        "country": "Singapore",
        "clues": [
            "This city-state is famous for its futuristic skyline.",
            "Has strict laws, including bans on chewing gum!"
        ],
        "fun_fact": [
            "Singapore’s Changi Airport has a waterfall inside a shopping mall.",
            "The Marina Bay Sands hotel has the world’s largest rooftop infinity pool."
        ],
        "trivia": [
            "Singapore is one of only three city-states in the world.",
            "It is known as the 'Garden City' due to its extensive greenery."
        ]
    },
    {
        "city": "Athens",
        "country": "Greece",
        "clues": [
            "This city is the birthplace of democracy.",
            "Home to an ancient temple dedicated to Athena."
        ],
        "fun_fact": [
            "Athens has been continuously inhabited for over 3,000 years.",
            "The Olympic Games originated in Greece."
        ],
        "trivia": [
            "The Parthenon was originally painted in bright colors, not just white marble.",
            "Athens has more theaters than any other city in the world."
        ]
    },
    {
        "city": "Buenos Aires",
        "country": "Argentina",
        "clues": [
            "Known as the 'Paris of South America'.",
            "The birthplace of the tango dance."
        ],
        "fun_fact": [
            "Buenos Aires has the widest avenue in the world, Avenida 9 de Julio.",
            "The Obelisk is one of its most famous landmarks."
        ],
        "trivia": [
            "The city has the highest number of bookstores per capita in the world.",
            "Its Teatro Colón is considered one of the best opera houses worldwide."
        ]
    },
    {
        "city": "Tokyo",
        "country": "Japan",
        "clues": [
            "The world's most populous metropolis.",
            "Home to the busiest pedestrian crossing in the world."
        ],
        "fun_fact": [
            "Tokyo was originally a small fishing village called Edo.",
            "There are more Michelin-starred restaurants here than in any other city."
        ],
        "trivia": [
            "Tokyo's Tsukiji Market was the world’s largest wholesale seafood market.",
            "The city experiences frequent mild earthquakes."
        ]
    },
    {
        "city": "London",
        "country": "United Kingdom",
        "clues": [
            "This city has a famous clock tower that is often mistaken for its bell.",
            "It was once the capital of the largest empire in history."
        ],
        "fun_fact": [
            "Big Ben actually refers to the bell, not the tower.",
            "London has more Indian restaurants than Mumbai!"
        ],
        "trivia": [
            "The London Underground is the oldest metro system in the world.",
            "The Queen’s official residence, Buckingham Palace, has over 700 rooms."
        ]
    },
    {
        "city": "New York City",
        "country": "United States",
        "clues": [
            "The city that never sleeps.",
            "Home to a famous green statue gifted by France."
        ],
        "fun_fact": [
            "Times Square was originally called Longacre Square.",
            "Central Park is larger than the country of Monaco."
        ],
        "trivia": [
            "NYC has the largest subway system by number of stations.",
            "The Empire State Building was the tallest in the world for nearly 40 years."
        ]
    },
    {
        "city": "Rio de Janeiro",
        "country": "Brazil",
        "clues": [
            "Famous for its annual carnival and colorful parades.",
            "Home to one of the New Seven Wonders of the World."
        ],
        "fun_fact": [
            "The iconic Christ the Redeemer statue is 30 meters tall.",
            "Rio’s Copacabana Beach has a famous black-and-white mosaic sidewalk."
        ],
        "trivia": [
            "Sugarloaf Mountain offers a breathtaking view of the city.",
            "Football (soccer) is a huge part of Rio’s culture."
        ]
    },
    {
        "city": "Sydney",
        "country": "Australia",
        "clues": [
            "Has a world-famous opera house shaped like sails.",
            "Home to one of the most famous beaches in the world."
        ],
        "fun_fact": [
            "Sydney's Harbour Bridge is nicknamed 'The Coathanger'.",
            "It is not Australia’s capital, despite popular belief."
        ],
        "trivia": [
            "Bondi Beach is one of the most visited beaches in the world.",
            "Sydney was founded as a British penal colony."
        ]
    },
    {
        "city": "Cairo",
        "country": "Egypt",
        "clues": [
            "Home to ancient pyramids that have stood for thousands of years.",
            "Located along the longest river in the world."
        ],
        "fun_fact": [
            "Cairo's Great Pyramid was the tallest man-made structure for over 3,800 years.",
            "The city is known as 'The City of a Thousand Minarets'."
        ],
        "trivia": [
            "The Nile River flows northward instead of southward.",
            "Cairo's Khan El-Khalili market is one of the oldest bazaars in the world."
        ]
    },
    {
        "city": "Istanbul",
        "country": "Turkey",
        "clues": [
            "This city lies on two continents.",
            "It was historically known as Byzantium and Constantinople."
        ],
        "fun_fact": [
            "The Grand Bazaar has over 4,000 shops.",
            "Istanbul's Hagia Sophia has served as a church, mosque, and museum."
        ],
        "trivia": [
            "The Bosphorus Strait separates Europe from Asia.",
            "Tulips were originally introduced to Europe from Istanbul."
        ]
    },
    {
        "city": "Bangkok",
        "country": "Thailand",
        "clues": [
            "Known for its floating markets and street food.",
            "Home to the Grand Palace and Wat Arun temple."
        ],
        "fun_fact": [
            "Bangkok’s full name is one of the longest city names in the world.",
            "The city is known as 'The Venice of the East' due to its canals."
        ],
        "trivia": [
            "Bangkok is home to the world’s largest solid gold Buddha statue.",
            "The city has over 400 temples."
        ]
    },
    {
        "city": "Barcelona",
        "country": "Spain",
        "clues": [
            "Famous for a basilica that has been under construction for over a century.",
            "Known for its love of football and art."
        ],
        "fun_fact": [
            "Barcelona’s La Rambla was once a river.",
            "Antoni Gaudí’s Sagrada Familia is still unfinished."
        ],
        "trivia": [
            "Barcelona is one of the most bike-friendly cities in Europe.",
            "The city hosted the 1992 Summer Olympics."
        ]
    },
    {
        "city": "Marrakech",
        "country": "Morocco",
        "clues": [
            "A famous city with red sandstone walls.",
            "Known for its bustling souks and snake charmers."
        ],
        "fun_fact": [
            "Marrakech’s Medina is a UNESCO World Heritage Site.",
            "The city’s Jemaa el-Fnaa square comes alive at night with street performances."
        ],
        "trivia": [
            "Marrakech is often called the 'Red City'.",
            "The city has been a cultural hub for over 1,000 years."
        ]
    },
    {
        "city": "Havana",
        "country": "Cuba",
        "clues": [
            "Famous for classic American cars and colorful buildings.",
            "A city known for its vibrant music and dance culture."
        ],
        "fun_fact": [
            "Havana has one of the world’s largest colonial-era fortresses.",
            "Cuba is known for producing the finest cigars."
        ],
        "trivia": [
            "Hemingway wrote 'The Old Man and the Sea' while living in Havana.",
            "The city has the world's only museum dedicated to rum."
        ]
    },
    {
        "city": "Reykjavik",
        "country": "Iceland",
        "clues": [
            "The northernmost capital city in the world.",
            "Famous for its geothermal hot springs and northern lights."
        ],
        "fun_fact": [
            "Reykjavik has no McDonald’s restaurants!",
            "The city uses geothermal energy for heating."
        ],
        "trivia": [
            "Iceland has more sheep than people.",
            "The city experiences nearly 24 hours of daylight in summer."
        ]
    },
    {
        "city": "Amsterdam",
        "country": "Netherlands",
        "clues": [
            "Famous for its canals, bicycles, and tulips.",
            "Home to the Anne Frank House and Van Gogh Museum."
        ],
        "fun_fact": [
            "Amsterdam has more bicycles than people.",
            "The city's canals stretch over 100 kilometers, earning it the nickname 'Venice of the North'."
        ],
        "trivia": [
            "Amsterdam’s houses are built on wooden poles driven into marshy ground.",
            "The Netherlands was the first country to legalize same-sex marriage in 2001."
        ]
    },
    {
        "city": "Berlin",
        "country": "Germany",
        "clues": [
            "A city that was once divided by a famous wall.",
            "Known for its vibrant nightlife and historic landmarks."
        ],
        "fun_fact": [
            "The Berlin Wall fell in 1989, uniting East and West Berlin.",
            "Berlin has more bridges than Venice."
        ],
        "trivia": [
            "Currywurst, a popular German street food, was invented in Berlin.",
            "Berlin’s underground train stations served as bunkers during World War II."
        ]
    },
    {
        "city": "Cape Town",
        "country": "South Africa",
        "clues": [
            "Famous for a flat-topped mountain overlooking the city.",
            "Located near the meeting point of the Atlantic and Indian Oceans."
        ],
        "fun_fact": [
            "Table Mountain is one of the New Seven Wonders of Nature.",
            "Cape Town was the first city outside Europe to get Blue Flag beaches."
        ],
        "trivia": [
            "Nelson Mandela was imprisoned on Robben Island, just off Cape Town's coast.",
            "The city produces some of the world's best wines."
        ]
    },
    {
        "city": "Moscow",
        "country": "Russia",
        "clues": [
            "Home to a famous red square and an iconic cathedral.",
            "The capital of the largest country in the world."
        ],
        "fun_fact": [
            "Moscow’s subway system is one of the most beautiful in the world, with chandeliers and mosaics.",
            "The Kremlin has been the seat of Russian power for centuries."
        ],
        "trivia": [
            "Moscow is one of the coldest capital cities in the world.",
            "The city has over 800 churches."
        ]
    },
    {
        "city": "Dubai",
        "country": "United Arab Emirates",
        "clues": [
            "Home to the tallest building in the world.",
            "Famous for its luxurious lifestyle and artificial islands."
        ],
        "fun_fact": [
            "Dubai’s Burj Khalifa is 828 meters tall.",
            "The city has an indoor ski resort in the desert."
        ],
        "trivia": [
            "Dubai has ATMs that dispense gold.",
            "The police force has supercars like Lamborghinis and Ferraris."
        ]
    },
    {
        "city": "Rome",
        "country": "Italy",
        "clues": [
            "Once the center of a great ancient empire.",
            "Home to a tiny independent country within its borders."
        ],
        "fun_fact": [
            "Rome has a museum dedicated entirely to pasta.",
            "The city’s Trevi Fountain collects about $1.5 million in coins yearly, which is donated to charity."
        ],
        "trivia": [
            "Vatican City, the world’s smallest country, is within Rome.",
            "The Colosseum once hosted gladiator fights for entertainment."
        ]
    },
    {
        "city": "Toronto",
        "country": "Canada",
        "clues": [
            "This city has the tallest freestanding structure in the Western Hemisphere.",
            "Home to one of the most multicultural populations in the world."
        ],
        "fun_fact": [
            "Over 50% of Toronto’s population was born outside Canada.",
            "The CN Tower was the world’s tallest free-standing structure until 2007."
        ],
        "trivia": [
            "Toronto’s PATH is the largest underground shopping complex in the world.",
            "The city’s name comes from an Indigenous word meaning 'place where trees stand in water'."
        ]
    },
    {
        "city": "Athens",
        "country": "Greece",
        "clues": [
            "The birthplace of democracy.",
            "Home to an ancient temple dedicated to a goddess of wisdom."
        ],
        "fun_fact": [
            "Athens has been continuously inhabited for over 3,000 years.",
            "The Parthenon was once used as a church, a mosque, and a gunpowder store."
        ],
        "trivia": [
            "The first modern Olympic Games were held in Athens in 1896.",
            "Greek is one of the oldest written languages still in use today."
        ]
    },
    {
        "city": "Buenos Aires",
        "country": "Argentina",
        "clues": [
            "Known as the 'Paris of South America'.",
            "The birthplace of a passionate dance style."
        ],
        "fun_fact": [
            "Buenos Aires has the widest avenue in the world, Avenida 9 de Julio.",
            "The city is home to the world's most beautiful bookstore, El Ateneo Grand Splendid."
        ],
        "trivia": [
            "Tango music and dance originated in Buenos Aires.",
            "Buenos Aires has the highest number of bookstores per capita in the world."
        ]
    },
    {
        "city": "Seoul",
        "country": "South Korea",
        "clues": [
            "A high-tech city famous for K-pop and Korean BBQ.",
            "Home to a palace that was the main royal residence during the Joseon dynasty."
        ],
        "fun_fact": [
            "Seoul has the fastest internet speeds in the world.",
            "The city’s subway stations have underground shopping malls."
        ],
        "trivia": [
            "The world's first cloned dog, Snuppy, was created in Seoul.",
            "South Korea is the only country with a special 'Kimchi Refrigerator'."
        ]
    },
    {
        "city": "Stockholm",
        "country": "Sweden",
        "clues": [
            "Built on 14 islands connected by over 50 bridges.",
            "Home to the Nobel Prize award ceremony."
        ],
        "fun_fact": [
            "Stockholm’s subway stations are considered an art gallery.",
            "The city’s Old Town, Gamla Stan, dates back to the 13th century."
        ],
        "trivia": [
            "Stockholm was the first city to launch a congestion pricing scheme in Europe.",
            "The city has over 100 museums, one of the highest per capita in the world."
        ]
    },
    {
        "city": "Mexico City",
        "country": "Mexico",
        "clues": [
            "A city built on a lake, originally an Aztec capital.",
            "Home to one of the largest squares in the world, Zócalo."
        ],
        "fun_fact": [
            "Mexico City sinks about 50 cm per year due to its soft ground.",
            "It has the second-highest number of museums in the world, after London."
        ],
        "trivia": [
            "Tacos al pastor, one of Mexico’s most famous dishes, was inspired by Lebanese shawarma.",
            "Frida Kahlo and Diego Rivera lived and worked in Mexico City."
        ]
    },
    {
        "city": "Singapore",
        "country": "Singapore",
        "clues": [
            "A small island nation known for its cleanliness and futuristic skyline.",
            "Home to the world-famous Marina Bay Sands hotel."
        ],
        "fun_fact": [
            "Singapore has a law banning chewing gum sales.",
            "The city has an airport with a massive indoor waterfall."
        ],
        "trivia": [
            "Singapore is one of the world's most densely populated countries.",
            "It has four official languages: English, Malay, Tamil, and Mandarin."
        ]
    },
    {
        "city": "Istanbul",
        "country": "Turkey",
        "clues": [
            "The only city in the world that spans two continents.",
            "Home to a famous blue mosque."
        ],
        "fun_fact": [
            "Istanbul’s Grand Bazaar is one of the oldest and largest covered markets in the world.",
            "The city was once called Byzantium and later Constantinople."
        ],
        "trivia": [
            "Istanbul has over 3,000 mosques.",
            "The Bosphorus Strait divides the European and Asian parts of the city."
        ]
    },
    {
        "city": "Kyoto",
        "country": "Japan",
        "clues": [
            "Famous for its thousands of ancient temples and shrines.",
            "Known for its traditional wooden houses and geisha culture."
        ],
        "fun_fact": [
            "Kyoto has over 2,000 temples and shrines.",
            "The city was once Japan’s capital for over 1,000 years."
        ],
        "trivia": [
            "The famous cherry blossom festival attracts millions of tourists.",
            "Kyoto was originally on the shortlist of cities to be bombed with an atomic bomb but was spared due to its cultural significance."
        ]
    },
    {
        "city": "Lisbon",
        "country": "Portugal",
        "clues": [
            "A coastal city known for its historic trams and pastel-colored buildings.",
            "Home to a famous custard tart dessert."
        ],
        "fun_fact": [
            "Lisbon is older than Rome and London.",
            "It was almost entirely destroyed by a massive earthquake in 1755."
        ],
        "trivia": [
            "Lisbon has one of the longest suspension bridges in Europe.",
            "Fado music, a melancholic Portuguese music genre, originated here."
        ]
    },
    {
        "city": "Rio de Janeiro",
        "country": "Brazil",
        "clues": [
            "Home to a giant statue of Jesus on a mountain.",
            "Known for its world-famous carnival festival."
        ],
        "fun_fact": [
            "The Christ the Redeemer statue is one of the New Seven Wonders of the World.",
            "Rio’s beaches, like Copacabana and Ipanema, are world-famous."
        ],
        "trivia": [
            "The Maracanã Stadium hosted two FIFA World Cup finals.",
            "Rio de Janeiro means 'January River' in Portuguese."
        ]
    },
    {
        "city": "Prague",
        "country": "Czech Republic",
        "clues": [
            "Nicknamed the ‘City of a Hundred Spires.’",
            "Home to the world’s oldest operating astronomical clock."
        ],
        "fun_fact": [
            "The Prague Castle is the largest ancient castle in the world.",
            "The city’s Charles Bridge is said to be haunted."
        ],
        "trivia": [
            "Prague was largely untouched by World War II, preserving its historic architecture.",
            "Beer is cheaper than water in some parts of the city."
        ]
    },
    {
        "city": "Bangkok",
        "country": "Thailand",
        "clues": [
            "Home to one of the world’s largest open-air markets.",
            "Famous for its floating markets and ornate temples."
        ],
        "fun_fact": [
            "Bangkok’s real name is one of the longest city names in the world.",
            "The city has more than 400 temples."
        ],
        "trivia": [
            "The Grand Palace was once the home of Thai kings.",
            "Street food in Bangkok is ranked among the best in the world."
        ]
    },
    {
        "city": "Edinburgh",
        "country": "Scotland",
        "clues": [
            "Home to a famous castle built on an extinct volcano.",
            "Hosts the world's largest arts festival every August."
        ],
        "fun_fact": [
            "Edinburgh is where Harry Potter was first written.",
            "The city’s underground vaults are believed to be haunted."
        ],
        "trivia": [
            "Edinburgh has more listed buildings than any other UK city.",
            "The Stone of Destiny, used in coronations, was kept here."
        ]
    },
    {
        "city": "Mumbai",
        "country": "India",
        "clues": [
            "The financial capital of India and home to Bollywood.",
            "Famous for a railway station that is a UNESCO World Heritage Site."
        ],
        "fun_fact": [
            "Mumbai was originally a group of seven islands.",
            "Dabbawalas deliver over 200,000 lunchboxes daily with near-perfect accuracy."
        ],
        "trivia": [
            "The Gateway of India was built to welcome King George V.",
            "The world’s most expensive private home, Antilia, is in Mumbai."
        ]
    },
    {
        "city": "Cairo",
        "country": "Egypt",
        "clues": [
            "A city with pyramids nearby.",
            "Home to the largest open-air museum in the world."
        ],
        "fun_fact": [
            "The Great Pyramid of Giza was the tallest man-made structure for over 3,800 years.",
            "Cairo is the largest city in Africa."
        ],
        "trivia": [
            "The ancient city of Memphis once stood where Cairo is now.",
            "The Nile River flows through the city."
        ]
    },
    {
        "city": "Hanoi",
        "country": "Vietnam",
        "clues": [
            "The capital of a Southeast Asian country with a history of war and peace.",
            "Home to a lake with a legendary turtle."
        ],
        "fun_fact": [
            "Hanoi’s Old Quarter has streets named after the goods sold there.",
            "The city has French colonial architecture due to past occupation."
        ],
        "trivia": [
            "Vietnamese coffee culture is famous worldwide.",
            "Hanoi is home to the world’s cheapest beer, Bia Hoi."
        ]
    },
    {
        "city": "Venice",
        "country": "Italy",
        "clues": [
            "A city with no roads, only canals.",
            "Famous for its masked carnival festival."
        ],
        "fun_fact": [
            "Venice is slowly sinking into the sea.",
            "The city’s main square floods regularly."
        ],
        "trivia": [
            "Gondoliers must undergo years of training.",
            "Venice’s oldest café, Caffè Florian, dates back to 1720."
        ]
    },
    {
        "city": "Los Angeles",
        "country": "USA",
        "clues": [
            "Home to Hollywood and the film industry.",
            "Famous for a large sign on a hill."
        ],
        "fun_fact": [
            "The Hollywood sign originally read ‘Hollywoodland.’",
            "Los Angeles has more cars than people."
        ],
        "trivia": [
            "LA was once part of Mexico.",
            "The city has the largest Thai population outside Thailand."
        ]
    },
    {
        "city": "Madrid",
        "country": "Spain",
        "clues": [
            "The capital of a country known for flamenco dancing.",
            "Home to one of the world's most successful soccer clubs."
        ],
        "fun_fact": [
            "Madrid is Europe’s highest capital city.",
            "The oldest restaurant in the world, Sobrino de Botín, is here."
        ],
        "trivia": [
            "Madrid’s main square, Plaza Mayor, has been used for bullfights.",
            "The city is home to the famous Prado Museum."
        ]
    },
    {
        "city": "Cape Town",
        "country": "South Africa",
        "clues": [
            "Famous for a flat-topped mountain.",
            "Home to a former prison island where Nelson Mandela was held."
        ],
        "fun_fact": [
            "Cape Town was the first city in Africa to host the FIFA World Cup.",
            "The city is home to one of the most diverse floral kingdoms in the world."
        ],
        "trivia": [
            "The Cape of Good Hope is located nearby.",
            "Table Mountain has its own unique cloud formation called the 'tablecloth.'"
        ]
    },
    {
        "city": "Seoul",
        "country": "South Korea",
        "clues": [
            "A city known for K-pop and cutting-edge technology.",
            "Home to one of the world's fastest internet speeds."
        ],
        "fun_fact": [
            "Seoul has the world's largest underground shopping mall.",
            "The city is home to five UNESCO World Heritage Sites."
        ],
        "trivia": [
            "The DMZ, the border with North Korea, is just an hour away.",
            "Seoul's subway system is one of the most efficient in the world."
        ]
    },
    {
        "city": "Vienna",
        "country": "Austria",
        "clues": [
            "Known as the city of music and home to famous composers.",
            "Has a café culture that is recognized by UNESCO."
        ],
        "fun_fact": [
            "Vienna was once the capital of the Austro-Hungarian Empire.",
            "The world’s oldest zoo is located here."
        ],
        "trivia": [
            "The famous Schönbrunn Palace has over 1,400 rooms.",
            "Vienna’s Prater Park is home to a historic Ferris wheel."
        ]
    },
    {
        "city": "Toronto",
        "country": "Canada",
        "clues": [
            "Home to one of the tallest freestanding towers in the world.",
            "A city known for its diversity and multiculturalism."
        ],
        "fun_fact": [
            "Toronto has a massive underground pedestrian walkway called PATH.",
            "The city is home to over 140 languages spoken daily."
        ],
        "trivia": [
            "Toronto’s sports teams include the Raptors and the Blue Jays.",
            "The city’s name comes from an Indigenous word meaning 'place where trees stand in water.'"
        ]
    },
    {
        "city": "Buenos Aires",
        "country": "Argentina",
        "clues": [
            "The birthplace of tango.",
            "Home to a famous pink presidential palace."
        ],
        "fun_fact": [
            "Buenos Aires has more bookstores per capita than any other city.",
            "The city’s widest avenue has 12 lanes."
        ],
        "trivia": [
            "Diego Maradona, one of football’s greatest players, was born here.",
            "Buenos Aires means 'fair winds' in Spanish."
        ]
    },
    {
        "city": "Athens",
        "country": "Greece",
        "clues": [
            "The birthplace of democracy.",
            "Home to an ancient temple dedicated to Athena."
        ],
        "fun_fact": [
            "The Olympic Games originated in Greece over 2,700 years ago.",
            "Athens is one of the world's oldest cities, with over 3,400 years of history."
        ],
        "trivia": [
            "The Acropolis was built in the 5th century BC.",
            "Ancient Greek philosophers like Socrates and Plato lived here."
        ]
    },
    {
        "city": "Stockholm",
        "country": "Sweden",
        "clues": [
            "Built on 14 islands connected by over 50 bridges.",
            "Home to the Nobel Prize ceremony."
        ],
        "fun_fact": [
            "Stockholm has an underground art gallery in its subway system.",
            "The city is known as the 'Venice of the North.'"
        ],
        "trivia": [
            "ABBA, one of the world’s best-selling music groups, is from Stockholm.",
            "The Vasa Museum houses a 17th-century warship that sank minutes after launching."
        ]
    },
    {
        "city": "Berlin",
        "country": "Germany",
        "clues": [
            "Once divided by a famous wall.",
            "Home to the Brandenburg Gate."
        ],
        "fun_fact": [
            "Berlin has more bridges than Venice.",
            "Currywurst, a popular street food, was invented here."
        ],
        "trivia": [
            "Berlin has the largest Turkish population outside Turkey.",
            "The Berlin Wall fell in 1989, reunifying the city."
        ]
    },
    {
        "city": "Dubai",
        "country": "United Arab Emirates",
        "clues": [
            "Home to the tallest building in the world.",
            "A city known for luxury and futuristic architecture."
        ],
        "fun_fact": [
            "Dubai has an indoor ski resort inside a mall.",
            "The Palm Jumeirah is a man-made island shaped like a palm tree."
        ],
        "trivia": [
            "Dubai's police force has supercars like Lamborghinis and Ferraris.",
            "Gold vending machines are found in shopping malls."
        ]
    },
    {
        "city": "Moscow",
        "country": "Russia",
        "clues": [
            "Home to a colorful cathedral with onion-shaped domes.",
            "The capital of the world’s largest country by land area."
        ],
        "fun_fact": [
            "Moscow’s metro stations look like underground palaces.",
            "The Kremlin is the largest active fortress in Europe."
        ],
        "trivia": [
            "The city experiences extreme temperature differences, from -30°C in winter to 30°C in summer.",
            "The Red Square has been a political and cultural center for centuries."
        ]
    },
    {
        "city": "Helsinki",
        "country": "Finland",
        "clues": [
            "A Nordic capital with a sauna culture.",
            "Known for its design and architecture."
        ],
        "fun_fact": [
            "Helsinki has more saunas than cars.",
            "The city was once ruled by both Sweden and Russia."
        ],
        "trivia": [
            "The world's first national park was established here in 1938.",
            "Helsinki is one of the cleanest cities in the world."
        ]
    },
    {
        "city": "Lima",
        "country": "Peru",
        "clues": [
            "A South American city famous for ceviche.",
            "Home to pre-Columbian pyramids in an urban setting."
        ],
        "fun_fact": [
            "Lima was once the wealthiest city in the Americas.",
            "The city experiences almost no rainfall despite being coastal."
        ],
        "trivia": [
            "The historic center is a UNESCO World Heritage Site.",
            "The city has a large Chinese-Peruvian population, influencing its cuisine."
        ]
    },
    {
        "city": "Kuala Lumpur",
        "country": "Malaysia",
        "clues": [
            "Home to twin towers that were once the tallest in the world.",
            "A melting pot of Malay, Chinese, and Indian cultures."
        ],
        "fun_fact": [
            "Kuala Lumpur means 'muddy confluence' in Malay.",
            "The Batu Caves have a massive golden statue at their entrance."
        ],
        "trivia": [
            "The city’s night markets are a paradise for food lovers.",
            "It is home to the largest indoor amusement park in Southeast Asia."
        ]
    },
    {
        "city": "Warsaw",
        "country": "Poland",
        "clues": [
            "A city rebuilt almost entirely after World War II.",
            "Home to a famous mermaid statue in its Old Town."
        ],
        "fun_fact": [
            "Warsaw's Old Town is a UNESCO World Heritage Site despite being reconstructed.",
            "The city’s name comes from a legendary fisherman and a mermaid."
        ],
        "trivia": [
            "Famous composer Frédéric Chopin was born near Warsaw.",
            "The Warsaw Uprising of 1944 was one of the largest resistance efforts in WWII."
        ]
    },
    {
        "city": "Jakarta",
        "country": "Indonesia",
        "clues": [
            "The capital city of the world's largest archipelago.",
            "Located on the island of Java."
        ],
        "fun_fact": [
            "Jakarta has one of the worst traffic congestions in the world.",
            "The city was formerly known as Batavia during Dutch colonial rule."
        ],
        "trivia": [
            "Jakarta is sinking at one of the fastest rates in the world.",
            "It is the most populous city in Southeast Asia."
        ]
    },
    {
        "city": "Mexico City",
        "country": "Mexico",
        "clues": [
            "Built on top of an ancient Aztec capital.",
            "One of the largest cities in the world."
        ],
        "fun_fact": [
            "The city sinks about 50 cm every year due to groundwater extraction.",
            "It has more museums than any other city in the world."
        ],
        "trivia": [
            "Frida Kahlo and Diego Rivera lived here.",
            "The city’s metro system is one of the cheapest in the world."
        ]
    },
    {
        "city": "Oslo",
        "country": "Norway",
        "clues": [
            "The capital of the country known for fjords.",
            "Home to the Nobel Peace Prize ceremony."
        ],
        "fun_fact": [
            "Oslo is one of the greenest capitals in Europe.",
            "The city is surrounded by forests and has a strong outdoor culture."
        ],
        "trivia": [
            "Oslo was called Christiania until 1925.",
            "It has the world’s most expensive Big Mac."
        ]
    },
    {
        "city": "Dublin",
        "country": "Ireland",
        "clues": [
            "Home to a famous dark stout beer.",
            "Its name means 'Black Pool' in Irish."
        ],
        "fun_fact": [
            "Dublin has the youngest population in Europe.",
            "The Guinness Storehouse is one of its top attractions."
        ],
        "trivia": [
            "Bram Stoker, the author of Dracula, was born here.",
            "Dublin’s Trinity College houses the Book of Kells."
        ]
    },
    {
        "city": "Manila",
        "country": "Philippines",
        "clues": [
            "A city in Southeast Asia known for jeepneys.",
            "Located on the island of Luzon."
        ],
        "fun_fact": [
            "The Philippines was a Spanish colony for over 300 years.",
            "Manila is one of the most densely populated cities in the world."
        ],
        "trivia": [
            "Rizal Park is named after a national hero.",
            "Intramuros is a walled city from the Spanish era."
        ]
    },
    {
        "city": "Casablanca",
        "country": "Morocco",
        "clues": [
            "The largest city in a North African country.",
            "Famous for a classic Hollywood movie with the same name."
        ],
        "fun_fact": [
            "Casablanca’s Hassan II Mosque has the tallest minaret in the world.",
            "The city is an economic hub of Morocco."
        ],
        "trivia": [
            "The city's name means 'White House' in Spanish.",
            "Rick's Café, inspired by the movie, was built years after the film was released."
        ]
    },
    {
        "city": "Edinburgh",
        "country": "Scotland",
        "clues": [
            "Famous for its annual arts festival.",
            "Home to a historic castle on a volcanic rock."
        ],
        "fun_fact": [
            "J.K. Rowling wrote much of Harry Potter in Edinburgh cafés.",
            "The city has more listed buildings than anywhere else in the UK."
        ],
        "trivia": [
            "Arthur's Seat is an extinct volcano within the city.",
            "It hosts the world’s largest arts festival, the Edinburgh Fringe."
        ]
    },
    {
        "city": "Hanoi",
        "country": "Vietnam",
        "clues": [
            "The capital of a Southeast Asian country with pho and banh mi.",
            "Home to the Ho Chi Minh Mausoleum."
        ],
        "fun_fact": [
            "Hanoi’s Old Quarter has 36 streets named after the goods they historically sold.",
            "Motorbikes outnumber cars by a significant margin."
        ],
        "trivia": [
            "Hoan Kiem Lake has a legend about a magical sword.",
            "Vietnamese coffee culture is strong here, with unique egg coffee."
        ]
    },
    {
        "city": "Nairobi",
        "country": "Kenya",
        "clues": [
            "A major African city with a national park inside its borders.",
            "Known as the 'Green City in the Sun.'"
        ],
        "fun_fact": [
            "Nairobi National Park is home to lions, rhinos, and giraffes.",
            "The city was originally a railway supply depot."
        ],
        "trivia": [
            "Nairobi’s name comes from the Maasai phrase 'cool water.'",
            "It is one of Africa’s major business and tech hubs."
        ]
    },
    {
        "city": "Bogotá",
        "country": "Colombia",
        "clues": [
            "The high-altitude capital of a South American country.",
            "Home to the famous Gold Museum."
        ],
        "fun_fact": [
            "Bogotá is one of the highest capitals in the world, at 2,640 meters.",
            "The city has a weekly event where streets are closed for cyclists and pedestrians."
        ],
        "trivia": [
            "Bogotá’s public transport includes the TransMilenio bus system.",
            "The city’s name comes from a Chibcha word meaning 'Lady of the Andes.'"
        ]
    },
    {
        "city": "Lisbon",
        "country": "Portugal",
        "clues": [
            "A European city known for its historic trams.",
            "Built on seven hills along a river."
        ],
        "fun_fact": [
            "Lisbon’s Vasco da Gama Bridge is the longest in Europe.",
            "The famous 'Pastel de Nata' was invented here."
        ],
        "trivia": [
            "Lisbon was devastated by a massive earthquake in 1755.",
            "The city’s Fado music is UNESCO-recognized."
        ]
    },
    {
        "city": "Kigali",
        "country": "Rwanda",
        "clues": [
            "A city known for its cleanliness and safety in Africa.",
            "The capital of the 'Land of a Thousand Hills.'"
        ],
        "fun_fact": [
            "Kigali has banned plastic bags since 2008.",
            "The city has one of the fastest-growing economies in Africa."
        ],
        "trivia": [
            "The Kigali Genocide Memorial honors victims of the 1994 genocide.",
            "The city is built on several rolling hills."
        ]
    },
    {
        "city": "Doha",
        "country": "Qatar",
        "clues": [
            "A Middle Eastern city that hosted the FIFA World Cup.",
            "Home to futuristic skyscrapers and the Museum of Islamic Art."
        ],
        "fun_fact": [
            "Doha was a small fishing village before rapid development.",
            "It has one of the highest GDP per capita in the world."
        ],
        "trivia": [
            "Pearl-Qatar is a man-made island shaped like an oyster.",
            "The city is built on reclaimed land."
        ]
    },
    {
        "city": "Santiago",
        "country": "Chile",
        "clues": [
            "A city at the foot of the Andes Mountains.",
            "The capital of a long, narrow South American country."
        ],
        "fun_fact": [
            "Santiago is home to South America’s tallest skyscraper.",
            "The city has frequent earthquakes but is built to withstand them."
        ],
        "trivia": [
            "The Mapocho River runs through the city.",
            "Pablo Neruda, the famous poet, had a house here."
        ]
    },
    {
        "city": "Islamabad",
        "country": "Pakistan",
        "clues": [
            "A planned city known for its greenery and wide roads.",
            "Home to the largest mosque in Pakistan."
        ],
        "fun_fact": [
            "Islamabad was built in the 1960s to replace Karachi as the capital.",
            "The city is located at the base of the Margalla Hills."
        ],
        "trivia": [
            "Faisal Mosque was funded by Saudi Arabia.",
            "It has one of the highest literacy rates in Pakistan."
        ]
    },
    {
        "city": "Muscat",
        "country": "Oman",
        "clues": [
            "A Middle Eastern capital with a scenic coastline.",
            "Home to the Sultan Qaboos Grand Mosque."
        ],
        "fun_fact": [
            "Muscat is one of the cleanest cities in the world.",
            "The city has a strict building height limit to maintain its skyline."
        ],
        "trivia": [
            "Mutrah Souq is one of the oldest markets in the region.",
            "The city has been a major trading hub for centuries."
        ]
    },
    {
        "city": "Kampala",
        "country": "Uganda",
        "clues": [
            "Built on seven hills in East Africa.",
            "The capital of a country with mountain gorillas."
        ],
        "fun_fact": [
            "The name comes from the local Impala antelope.",
            "Boda bodas (motorcycle taxis) are the most popular mode of transport."
        ],
        "trivia": [
            "Kampala was the headquarters of the Buganda Kingdom.",
            "It’s home to the Kasubi Tombs, a UNESCO World Heritage Site."
        ]
    },
    {
        "city": "Montevideo",
        "country": "Uruguay",
        "clues": [
            "A South American city known for its long beach promenade.",
            "The capital of a country famous for its football and mate tea."
        ],
        "fun_fact": [
            "Montevideo has more bookshops per capita than any other city in Latin America.",
            "The city was founded by the Spanish in the 18th century."
        ],
        "trivia": [
            "The Mercado del Puerto is a famous spot for Uruguayan barbecue.",
            "Montevideo is one of the safest capitals in South America."
        ]
    },
    {
        "city": "Addis Ababa",
        "country": "Ethiopia",
        "clues": [
            "A city located in the Horn of Africa.",
            "Home to the headquarters of the African Union."
        ],
        "fun_fact": [
            "Addis Ababa means 'New Flower' in Amharic.",
            "The city has Africa’s largest open-air market, Merkato."
        ],
        "trivia": [
            "Ethiopian time follows a 12-hour clock system starting at sunrise.",
            "Lucy, one of the oldest human fossils, was discovered in Ethiopia."
        ]
    },
    {
        "city": "Tashkent",
        "country": "Uzbekistan",
        "clues": [
            "A Silk Road city in Central Asia.",
            "The capital of the most populous country in the region."
        ],
        "fun_fact": [
            "Tashkent has a beautiful Soviet-era metro system.",
            "It was heavily rebuilt after a massive earthquake in 1966."
        ],
        "trivia": [
            "The city has a large number of fountains.",
            "Chorsu Bazaar is one of the most famous markets in Central Asia."
        ]
    },
    {
        "city": "Minsk",
        "country": "Belarus",
        "clues": [
            "The capital of a landlocked Eastern European country.",
            "Known for its Soviet-style architecture."
        ],
        "fun_fact": [
            "Minsk was almost entirely rebuilt after World War II.",
            "It has one of the world’s cleanest metro systems."
        ],
        "trivia": [
            "The city was part of the Grand Duchy of Lithuania in medieval times.",
            "Victory Square features a massive obelisk and eternal flame."
        ]
    },
    {
        "city": "Ulaanbaatar",
        "country": "Mongolia",
        "clues": [
            "One of the coldest capitals in the world.",
            "Located between Russia and China."
        ],
        "fun_fact": [
            "More than half of Mongolia’s population lives here.",
            "The city is home to the world’s largest equestrian statue of Genghis Khan."
        ],
        "trivia": [
            "Ulaanbaatar means 'Red Hero' in Mongolian.",
            "It started as a nomadic Buddhist monastery."
        ]
    },
    {
        "city": "Havana",
        "country": "Cuba",
        "clues": [
            "A Caribbean city famous for classic cars and cigars.",
            "Its old town is a UNESCO World Heritage Site."
        ],
        "fun_fact": [
            "Havana was once one of the wealthiest cities in the Americas.",
            "The Malecon is a popular seaside boulevard."
        ],
        "trivia": [
            "Hemingway wrote much of his work here.",
            "El Capitolio resembles the U.S. Capitol building."
        ]
    },
    {
        "city": "Reykjavik",
        "country": "Iceland",
        "clues": [
            "The northernmost capital of a sovereign country.",
            "Known for its colorful houses and geothermal pools."
        ],
        "fun_fact": [
            "Reykjavik is powered almost entirely by renewable energy.",
            "It has no McDonald's restaurants."
        ],
        "trivia": [
            "The city's name means 'Smoky Bay.'",
            "The Sun Voyager sculpture is a famous landmark."
        ]
    },
    {
        "city": "Windhoek",
        "country": "Namibia",
        "clues": [
            "The capital of a Southern African country with a desert.",
            "Home to German colonial architecture."
        ],
        "fun_fact": [
            "Namibia is one of the least densely populated countries in the world.",
            "Windhoek means 'Windy Corner' in Afrikaans."
        ],
        "trivia": [
            "Christuskirche is one of its most iconic buildings.",
            "The city has a strong beer culture due to its German influence."
        ]
    },
    {
        "city": "Tbilisi",
        "country": "Georgia",
        "clues": [
            "A city famous for its sulfur baths.",
            "Located at the crossroads of Europe and Asia."
        ],
        "fun_fact": [
            "Tbilisi’s name comes from the Georgian word for 'warm place.'",
            "The city is known for its eclectic mix of architecture."
        ],
        "trivia": [
            "The city’s cable cars offer stunning views of the Old Town.",
            "Georgia is considered the birthplace of wine."
        ]
    },
    {
        "city": "Baku",
        "country": "Azerbaijan",
        "clues": [
            "The capital city on the Caspian Sea.",
            "Famous for the futuristic Flame Towers."
        ],
        "fun_fact": [
            "Baku is the lowest-lying national capital in the world.",
            "It has one of the world’s largest oil reserves."
        ],
        "trivia": [
            "The old city, Icherisheher, is a UNESCO World Heritage Site.",
            "Mud volcanoes are common in the surrounding areas."
        ]
    }
]

class Command(BaseCommand):
    help = "Load destination data into the database"

    def handle(self, *args, **kwargs):
        for item in data:
            Destination.objects.create(
                city=item["city"],
                country=item["country"],
                clues=item["clues"],
                fun_fact=item["fun_fact"],
                trivia=item["trivia"]
            )
        self.stdout.write(self.style.SUCCESS("Successfully loaded destination data!"))
