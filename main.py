import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
from konlpy.tag import Okt

# Initialize the Korean text processor
okt = Okt()

# Load the text file
text = open(r"./data/South Korea Constitution.txt", mode="r", encoding="utf-8").read()
words = okt.nouns(text)
cleaned_text = " ".join(words)

# The Image shape in which you want to convert it to.
mask = np.array(Image.open(r"./images/Heart Shape Image.jpeg"))

# Create WordCloud object
wc = WordCloud(
    stopwords=STOPWORDS,
    mask=mask,
    font_path="./Nanum Gothic/NanumGothic-Regular.ttf",
    background_color="white",
    max_words=2000,
    max_font_size=500,
    random_state=42,
    width=mask.shape[1],
    height=mask.shape[0],
)

# Generate the wordcloud from the cleaned text
wc.generate(cleaned_text)

# Show the wordcloud
plt.imshow(wc, interpolation="None")
plt.axis("off")

# Save the wordcloud image to the 'results' folder
wc.to_file("./results/wordcloud.png")

# Display the wordcloud
plt.show()
