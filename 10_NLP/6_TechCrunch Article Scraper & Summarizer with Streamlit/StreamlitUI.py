import streamlit as st  # Streamlit library for building the web UI
from transformers import pipeline  # Hugging Face Transformers for text summarization
import requests  # Library for making HTTP requests to fetch web content
from bs4 import BeautifulSoup  # BeautifulSoup for parsing HTML content
from docx import Document  # python-docx library for creating Word documents

# Configure the Streamlit page settings
st.set_page_config(page_title="TechCrunch Summarizer", layout="wide")  # Set page title and use wide layout for better UI

# Initialize the summarization model
# Load the BART-large-CNN model from Hugging Face for summarizing text
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define constants for web scraping
# HTTP headers to mimic a browser and avoid being blocked by websites
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"}
# Base URL for TechCrunch, used for fetching articles
TECHCRUNCH_URL = "https://techcrunch.com"

# Inject custom CSS into the Streamlit app for styling
# Define font size classes for consistent typography across the UI
st.markdown("""
    <style>
    .big-font {
        font-size: 24px !important;  /* Large font for titles */
        font-weight: bold;  /* Bold text for emphasis */
    }
    .medium-font {
        font-size: 18px !important;  /* Medium font for labels */
    }
    .small-font {
        font-size: 14px !important;  /* Small font for detailed content */
    }
    </style>
    """, unsafe_allow_html=True)

# Define function to fetch article content from a URL
def get_article_content(url):
    """Fetch and return the full content of an article given its URL."""
    try:
        # Send an HTTP GET request to the provided URL with browser-like headers
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error if the request fails (e.g., 404, 500)
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the div containing the article content (assumes class "entry-content")
        content_div = soup.find('div', {"class": "entry-content"})
        if not content_div:
            # Warn the user if no content div is found
            st.warning(f"Could not find article content in the URL: {url}")
            return None
        
        # Extract all paragraph tags within the content div
        paragraphs = content_div.find_all('p')
        # Join paragraph texts with newlines and remove leading/trailing whitespace
        return '\n'.join(p.get_text() for p in paragraphs).strip()
    except Exception as e:
        # Display an error message if fetching fails (e.g., network issues)
        st.error(f"Error fetching article content: {e}")
        return None

# Define function to scrape latest articles from TechCrunch
def get_latest_articles(num_articles=3):
    """Scrapes TechCrunch’s homepage for the latest articles."""
    articles = []  # List to store article dictionaries
    try:
        # Fetch the TechCrunch homepage
        response = requests.get(TECHCRUNCH_URL, headers=HEADERS)
        response.raise_for_status()  # Check for request success
        # Parse the homepage HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find article cards (limited to num_articles), assuming class "post-card"
        article_cards = soup.find_all("article", {"class": "post-card"}, limit=num_articles)
        for card in article_cards:
            # Extract the article title from the h2 tag with class "post-card__title"
            title_tag = card.find("h2", class_="post-card__title")
            link_tag = title_tag.find("a") if title_tag else None  # Get the link if title exists
            title = link_tag.get_text(strip=True) if link_tag else "No Title Found"  # Default title if not found
            url = link_tag['href'] if link_tag else None  # Extract URL from the link
            
            if url:
                # Fetch the full content of the article
                full_content = get_article_content(url)
                if full_content:
                    # Add article details to the list if content is successfully fetched
                    articles.append({"title": title, "url": url, "full_content": full_content})
        return articles  # Return the list of articles
    except Exception as e:
        # Show error if scraping fails
        st.error(f"Error fetching latest articles: {e}")
        return []  # Return empty list on failure

# Define function to summarize text using the BART model
def summarize_text(text, max_length=150, min_length=50):
    """Summarizes the given text using BART."""
    # Check if the text is too short to summarize (less than 50 words)
    if len(text.split()) < 50:
        return "The article is too short to summarize."
    # Generate summary with specified max and min lengths, no sampling for consistency
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']  # Return the summarized text

# Define function to prepare summary for download
def create_downloadable_file(summary, format="txt"):
    """Prepare the summary content for download."""
    if format == "txt":
        # Convert summary to bytes for text file download
        return summary.encode()  # Return bytes for text file
    elif format == "docx":
        # Create a new Word document
        doc = Document()
        # Add the summary as a paragraph
        doc.add_paragraph(summary)
        import io  # Import io module for in-memory file handling
        buffer = io.BytesIO()  # Create a bytes buffer
        doc.save(buffer)  # Save the document to the buffer
        buffer.seek(0)  # Reset buffer position to the start
        return buffer.getvalue()  # Return bytes for docx file

# Define the main application function
def main():
    # Logo at the top of the page
    # Display a logo at the top of the app (replace with actual file path or URL)
    st.image("logo.png", width=150)  # Add your logo file in the same directory or use a URL
    
    # Display the app title with custom large font
    st.markdown('<p class="big-font">TechCrunch Article Summarizer</p>', unsafe_allow_html=True)
    
    # Sidebar configuration without section titles
    with st.sidebar:
        # Slider to select the number of articles to fetch (1 to 5, default 3)
        num_articles = st.slider("Number of Articles", 1, 5, 3)
        # Text input for a custom TechCrunch article URL
        custom_url = st.text_input("Enter a TechCrunch article URL")
        # Slider for maximum summary length (50 to 300 words, default 150)
        max_length = st.slider("Max Summary Length", 50, 300, 150)
        # Slider for minimum summary length (10 to 100 words, default 50)
        min_length = st.slider("Min Summary Length", 10, 100, 50)
        # Button to trigger summarization
        summarize_button = st.button("Summarize")
        # Dropdown to select export format (txt or docx)
        export_format = st.selectbox("Export Summary As", ["txt", "docx"])
        # Note: Export button is intentionally commented out as per original code
    
    # Display a logo in the sidebar (optional, replace with actual file path or URL)
    st.sidebar.image("logo.png", width=100)

    # Fetch the latest articles based on user input
    articles = get_latest_articles(num_articles)
    if custom_url:
        # Validate if the custom URL is from TechCrunch
        if not custom_url.startswith(TECHCRUNCH_URL):
            st.warning("Please enter a valid TechCrunch URL.")
        else:
            # Fetch content for the custom URL
            custom_article = get_article_content(custom_url)
            if custom_article:
                # Add custom article to the list
                articles.append({"title": "Custom Article", "url": custom_url, "full_content": custom_article})
    
    # Check if any articles were fetched
    if not articles:
        st.error("No articles found. Please check the URL or try again later.")
        return  # Exit the function if no articles are available
    
    # Dropdown to select an article from the fetched list
    st.markdown('<p class="medium-font">Select an article</p>', unsafe_allow_html=True)
    selected_title = st.selectbox("", [a["title"] for a in articles])  # Empty label for cleaner UI
    # Find the selected article from the list
    selected_article = next((a for a in articles if a["title"] == selected_title), None)
    
    if selected_article:
        # Display the selected article's title with large font
        st.markdown(f'<p class="big-font">{selected_article["title"]}</p>', unsafe_allow_html=True)
        # Provide a clickable link to the full article
        st.write(f"[Read full article]({selected_article['url']})")
        
        # Expander to show the full article content
        with st.expander("Show Full Article"):
            # Display full content with small font
            st.markdown(f'<p class="small-font">{selected_article["full_content"]}</p>', unsafe_allow_html=True)
        
        # Handle summarization and export when the summarize button is clicked
        if summarize_button:
            with st.spinner("Summarizing..."):  # Show a loading spinner during summarization
                # Generate the summary for the selected article
                summary = summarize_text(selected_article['full_content'], max_length=max_length, min_length=min_length)
                # Indicate successful summary generation
                st.success("Summary Generated!")
                # Display the summary label with medium font
                st.markdown('<p class="medium-font">Summary:</p>', unsafe_allow_html=True)
                # Display the summary text with small font
                st.markdown(f'<p class="small-font">{summary}</p>', unsafe_allow_html=True)
                
                # Prepare and provide a download button for the summary
                file_data = create_downloadable_file(summary, format=export_format)
                st.download_button(
                    label="Export Summary",  # Button label
                    data=file_data,  # File data in bytes
                    file_name=f"summary.{export_format}",  # Dynamic file name based on format
                    mime="text/plain" if export_format == "txt" else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"  # MIME type for download
                )

# Entry point of the application
if __name__ == "__main__":
    main()  # Run the main function when the script is executed