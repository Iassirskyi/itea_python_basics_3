V_1 = 'It’s a busy autumn morning at the Spanish Nursery, a bilingual nursery school in north London. Parents help their toddlers out of cycling helmets and jackets. Teachers greet the children with a cuddle and a chirpy “Buenos dias!”. In the playground, a little girl asks for her hair to be bunched up into a “coleta” (Spanish for “pigtail”), then rolls a ball and shouts “Catch!” in English. “At this age, children don’t learn a language – they acquire it,” says the school’s director Carmen Rampersad. It seems to sum up the enviable effortlessness of the little polyglots around her. For many of the children, Spanish is a third or even fourth language. Mother tongues include Croatian, Hebrew, Korean and Dutch. Compare this to the struggle of the average adult in a language class, and it would be easy to conclude that it’s best to start young. But science offers a much more complex view of how our relationship with languages evolves over a lifetime – and there is much to encourage late beginners.'
V_2 = 'SINGAPORE — It took Singapore, an island city-state of nearly 5 million people in southeast Asia, about 50 years to transform from a poor outpost into one of the most prosperous countries in the world. For a tourist, two days will be enough to fall in love with this Asian paradise. The city-state only gained independence from Malaysia in 1965 and immediately started its ascent into the club of the world’s richest and safest countries. Lee Kuan Yew, the country’s first prime minister, initiated huge changes and established the key factors that led to Singapore’s success: meritocracy, pragmatism and honesty. Now, guided by these rules, Singapore is leading the world’s rankings in education, ease of doing business, happiness, economic freedom and more. It is indeed unlike any other state in the world: a city of innovation, commerce and delicious food, where modern technologies mix with ancient traditions. Even though Singapore is an expensive city for travelers (prepare to spend up to $100 per day per person on food and entertainment), it is worth the money. And it is one of the best places to escape the cold Ukrainian winter. The weather in Singapore is pretty much hot and humid all year around. I traveled to Singapore at the beginning of January, during the rainy season. But in my case, even the occasional tropical rains could not spoil a weekend in this heavenly place.'
V_3 = '''A kaleidoscope of traditions, culture and vibrant geographies, India speaks for itself as a soul-stirring journey. From its dusty snow trenches, frolic coasts, gripping natural greens to the mystic ravines of spirituality and clusters of cultural shades, India captures the heart of every tourist. Bounded by the Himalayan ranges in the north and surrounded on three sides by water (Arabian sea, Bay of Bengal and Indian Ocean), India offers a wide array of places to see and things to do. The enchanting backwaters, hill stations and landscapes make India a beautiful country. Historical monuments, forts etc. add to the grandeur of the country. A country where at places temperature can reach as high as +50 degree celsius and at other places dip as low as -48 degree celsius, where you can find yourself in dense green forests or choose to be in a barren desert, go for a leisurely stroll in friendly neighborhood or indulge in adventure sports, whether you like the luxurious living of 5 star hotels or the pocket friendly budget accommodation – no matter what you like and looking for, India has it all.
The Indian tourist destinations have been broadly divided in 5 regions, North, East, West, South and North-East:
NORTH: Covers Delhi, Haryana, Himachal Pradesh, Jammu & Kashmir, Ladakh, Punjab, Rajasthan, Uttarakhand, Uttar Pradesh. It is here that both the hottest (in Rajasthan) and the coldest (in Jammu & Kashmir) places of India are located. The mesmerizing Taj Mahal and heritage hotels in Rajasthan’s palaces are located in this region. The magnificent Himalayas, the highest mountains in the world, are a treasure trove of mystery and spiritual knowledge, which they openly share with seekers willing to embrace them. The mountains in Uttarakhand and Himachal Pradesh offer challenging trekking, para-gliding, river rafting and many other adventure sports. The cultural epicentre of ancient India, Varanasi – also known as the City of Moksha – lies in the this region.
EAST: Covers Bihar, Jharkhand, Odisha, West Bengal and Andaman & Nicobar Islands. Bihar is known as ancient India’s centre of power, learning and culture, and is birthplace of Buddhism. Jharkhand is known for abundant forests, hills, wildlife, Paitkar Paintings, handicrafts and wood carvings. In Odisha you will come across its serpentine rivers, virgin beaches, mighty waterfalls and blue hills. The famous Konark Sun Temple and Jagannauth Yatra are major attractions. West Bengal is the State of Rabindranath Tagore. The capital city Kolkata is synonymous with mouth-watering street food. The fragrant mangrove forests of Sundarbans are the habitat of the famous Royal Bengal Tiger. The Andaman and Nicobar is an archipelago of more than 572 islands that offer peace, nature and beauty at its very best.
NORTH EAST: This region encompasses mountainous states of Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland and Sikkim. The region is replete with picturesque peaks and scenic rivers, beautiful Buddhist monasteries and almost impenetrable forests. Assam is a hot-spot for wild life tourism with over 25 national parks and sanctuaries. Manipur’s rich culture excels in martial arts, dance and theatre. Meghalaya which means Abode of the Clouds, is a once-in-a-lifetime experience. Mawsynram in Meghalaya receives the highest rainfall in the world. The poetic juxtaposition of mountains, valleys, rivers and lakes seems to be the cue for Mizoram’s beautiful music and dance. Nagaland lies nestled amongst the three mountain ranges of Naga, Patkai and Barail. Unique crafts like colourful woven shawls, mats, bamboo works, decorative spears and tribal song and dance distinguish various tribes. Sikkim’s mountains are a paradise for trekkers and adventurers. Trekking trails lead to hidden lakes and ancient monasteries.'''

initial_text = V_3
EXCEPTIONS = ('of', 'for', 'the', 'a', 'as', 'an', 'at', 'the', 'in', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my')
PUNCTUATIONS = ('+', '-', '&', '.', '!', '?', ',', ':', '—', '–', '“', '”', '"', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$')


def prettify_text(text):
    """
    This function removes from text specified exceptions and converts it into list
    :param text: unformated initial text
    :type text: str
    :return: cleaned elements of text
    :return: list
    """
    for element in PUNCTUATIONS:
        text = text.replace(element,'')

    text = text.lower().split()
    clean_text = text.copy()

    for element in text:
        if element in list(EXCEPTIONS):
            clean_text.remove(element)
       
    return clean_text


def words_count (text):
    return len (text)


def unique_words (text):
    """
    This function generate a list of unique elements of text in alphabetical order
    :param text: is a text formated as a list of elements 
    :type text: list
    :return: set of unique elements
    :return: set
    """
    text_dict = set (text)
    text_dict = sorted(text_dict)
    return text_dict
    
def f_words (text):
    """
    This function returns the most frequent elements of the text and quantity of it's occurance
    :param text: list of text elements 
    :type text: list
    :return: top 3 most frequent elements of the text and quantity of it's occurance
    :return: tuple
    """
    def counter (element):
        return text.count(element)
           
    frequency_list = sorted(unique_words(text), key=counter, reverse=True)
    
    top_1 = frequency_list[0], counter(frequency_list[0])
    top_2 = frequency_list[1], counter(frequency_list[1])
    top_3 = frequency_list[2], counter(frequency_list[2])
    
    return top_1, top_2, top_3


def frequency_calculation (element, text):
    """
    This function calculates percentage of element's occurance into text
    :param element: some element of the text
    :param text: list of text elements
    :type element: str
    :type text: list
    :return: percentage of element's occurance into text
    :return: float
    """
    basic_len = len(text)
    unique_list = unique_words(text)
    percentage = (text.count(element) / basic_len)

    return percentage


normalized_text = (prettify_text(initial_text))

print (f'This text consists of {words_count(normalized_text)} words.')

print (f'\nHere are those words: ')
for element in unique_words(normalized_text):
    print (element.capitalize(), end ='; ')

print ('\n\nThree most frequent words in this text are: ')
for i in range (3):
    if f_words(normalized_text)[i][1] == 1:
        print (f'{i+1}) Word "{(f_words(normalized_text)[i][0]).capitalize()}" meets {f_words(normalized_text)[i][1]} time;')
    else:
        print (f'{i+1}) Word "{(f_words(normalized_text)[i][0]).capitalize()}" meets {f_words(normalized_text)[i][1]} times;')

print ('\nHere is the frequency of each unique word in this text:')
for element in unique_words(normalized_text):
    percentage = frequency_calculation(element, normalized_text)
    print(f'{element} - {percentage:.2%}',end=', ')
