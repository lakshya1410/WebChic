# WebChic.ai 🎀

WebChic.ai is an AI-powered fashion advisor that provides personalized outfit analysis and recommendations. Built with Streamlit and powered by Google's Gemini AI, this web application helps users make informed decisions about their outfit choices by analyzing uploaded images and providing detailed styling advice.

## Features ✨

- **Outfit Analysis**: Upload any outfit photo and receive detailed feedback
- **Seasonal Recommendations**: Get advice on the best time of year to wear your outfit
- **Occasion Matching**: Learn which events and settings best suit your ensemble
- **Accessory Suggestions**: Receive personalized recommendations for complementary accessories
- **Time-of-Day Guidance**: Understand whether your outfit is better suited for day or night
- **Style Categorization**: Get insights into your outfit's style category

## Prerequisites

Before running the application, make sure you have:

- Python 3.7 or higher
- A Google API key for Gemini AI
- The required Python packages (listed in Requirements)

## Requirements

```
python-dotenv
streamlit
google.generativeai
Pillow
```

## Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd webchic-ai
```

2. Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run chic.py
```

## Usage

1. Launch the application using the command above
2. Upload an image of an outfit using the file uploader
3. Click the "Analyze Outfit" button
4. Wait for the AI to process your image
5. Review the detailed analysis and recommendations

## Features in Detail

### Image Analysis
- Supports JPG, JPEG, and PNG formats
- Automatically resizes images while maintaining aspect ratio
- Maximum height of 500 pixels for optimal performance

### AI Analysis Includes
- Best months to wear the outfit
- Suitable times of day
- Appropriate occasions
- Style categorization
- Complementary accessory suggestions

## UI Features

- Responsive design with a modern gradient theme
- Clear and intuitive user interface
- Loading spinner during analysis
- Organized two-column layout
- Custom styling for better visual hierarchy

## Customization

The application includes custom CSS styling that can be modified in the `st.markdown` section of the code. Key customizable elements include:

- Color schemes
- Font sizes
- Button styles
- Layout spacing
- Text formatting

## Technical Details

- Built with Streamlit for the frontend
- Uses Google's Gemini 2.0 Flash model for image analysis
- Implements environment variable management with python-dotenv
- Features responsive design with custom CSS
- Includes error handling for file uploads

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Support

For support, please contact me on tripathilakshya9@gmail.com

## Acknowledgments

- Google Generative AI for powering the image analysis
- Streamlit for the web framework
