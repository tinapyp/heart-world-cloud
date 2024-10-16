# Word Cloud Generator with Custom Shape

This project generates a word cloud from the South Korean Constitution text using a custom heart-shaped image as a mask. The project leverages the `wordcloud` library, `konlpy` for Korean text processing, and `Pillow` for image manipulation.

## Features

- **Korean Text Processing**: Extracts only the nouns from the input Korean text using `konlpy`'s `Okt` module.
- **Custom Shape Word Cloud**: Generates a word cloud that fits into a given image shape (in this case, a heart).
- **Stopword Removal**: Excludes common stopwords from the word cloud to ensure meaningful words dominate.

## Prerequisites

To run the code, you need to install the following Python libraries:

```bash
pip install wordcloud konlpy numpy pillow matplotlib
```

You also need the following files in the specified directories:

1. `./data/South Korea Constitution.txt` - The input text file (in Korean) from which the word cloud is generated.
2. `./images/Heart Shape Image.jpeg` - The heart-shaped image mask used for generating the word cloud.
3. `./Nanum Gothic/NanumGothic-Regular.ttf` - The font file for rendering Korean characters in the word cloud.

## How It Works

1. **Korean Text Processing**: The script uses `konlpy`'s `Okt` module to process the input Korean text, extracting only nouns to form the word cloud content.
2. **Image Mask**: A heart-shaped image is read using `PIL.Image` and transformed into a mask that determines the shape of the final word cloud.
3. **Word Cloud Generation**: The `WordCloud` class from the `wordcloud` library is used to generate the word cloud. Key parameters include:

   - `mask`: Defines the shape of the word cloud.
   - `stopwords`: A set of words to be excluded from the word cloud.
   - `font_path`: Path to the font that supports Korean characters.
   - `background_color`: The background color of the word cloud image.
   - `max_words`: The maximum number of words to include in the cloud.
   - `max_font_size`: The maximum size of the words in the cloud.
   - `width` & `height`: The size of the output image, determined by the mask.

4. **Visualization**: The generated word cloud is displayed using `matplotlib`.

## Usage

1. **Prepare the Text and Image**: Place the `South Korea Constitution.txt` and `Heart Shape Image.jpeg` in the appropriate directories.
2. **Run the Script**: Run the Python script in your terminal or IDE. The word cloud will be displayed as output.

## Customization

- **Change Shape**: You can use any other image to change the shape of the word cloud. Replace `Heart Shape Image.jpeg` with your preferred shape.
- **Adjust Word Cloud Parameters**: You can modify the maximum number of words, font size, or background color in the `WordCloud` object to customize the appearance.

## Output

The final output is a word cloud image shaped like a heart, generated from the South Korea Constitution text.
