import tkinter as tk
from tkinter import ttk
from transformers import pipeline
from mtranslate import translate
import ssl

class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Homepage")
        self.geometry("400x200+500+300")  # Set window size and position

       # Create buttons for accessing the translation page and the sentiment analysis page
        self.translate_button = ttk.Button(self, text="Translator", command=self.open_translator)
        self.translate_button.pack(pady=10)

        self.sentiment_button = ttk.Button(self, text="Text Sentiment Analyser", command=self.open_sentiment_analysis)
        self.sentiment_button.pack(pady=10)
      
    def open_translator(self):
        # Go to the translation page
        translator_page = LanguageTranslatorApp(self)
        translator_page.mainloop()
         
    def open_sentiment_analysis(self):
        # Go to the sentiment analysis page
        sentiment_page = SentimentAnalysisApp(self)
        sentiment_page.mainloop()

class LanguageTranslatorApp(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Translate Assistant")
        self.geometry("400x200+500+300")  # Set window size and position
        self.master = master

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.label_input = ttk.Label(self, text="Enter text to translate:")
        self.label_input.pack()
        #Creating input boxes
        self.input_text = tk.Text(self, height=4)
        self.input_text.pack()
        #Create translate button
        self.translate_button = ttk.Button(self, text="Translate", command=self.translate_text)
        self.translate_button.pack()
        #Creating labels to be entered
        self.result_label = ttk.Label(self, text="Waiting for text to be entered...")
        self.result_label.pack()
        #Creating the back button
        self.back_button = ttk.Button(self, text="Back", command=self.back_to_homepage)
        self.back_button.pack(pady=10)

    def translate_text(self):
        user_input = self.input_text.get("1.0", tk.END).strip()  # 获取用户输入的文本
        if user_input:
            translation = translate(user_input, 'en', 'zh')  # 使用翻译库进行翻译，从英语到中文
            self.display_result(translation)
        else:
            self.result_label.config(text="Error: Please enter text to translate")

    def display_result(self, translation):
        self.result_label.config(text=f"Translation: {translation}")

    def back_to_homepage(self):
        self.destroy()
        self.master.deiconify()
#Above is Xingcan Yan's part
#Below is Hongji Liu's Part
class SentimentAnalysisApp(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Sentiment Analysis")
        self.geometry("400x200+500+300") # Set window size and position 
        self.master = master

        # Use of sentiment analysis models
        self.sentiment_analyzer = pipeline("sentiment-analysis")

        self.create_widgets()

    def create_widgets(self):
        self.label_input = ttk.Label(self, text="Enter text to analyze:")
        self.label_input.pack()
        
        self.input_text = tk.Text(self, height=4)
        self.input_text.pack()

        self.analyze_button = ttk.Button(self, text="Analyze", command=self.analyze_sentiment)
        self.analyze_button.pack()

        self.result_label = ttk.Label(self, text="Waiting for text to be entered...")
        self.result_label.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.back_to_homepage)
        self.back_button.pack(pady=10)

    def analyze_sentiment(self):
        text_to_analyze = self.input_text.get("1.0", tk.END).strip()  # Get the text entered by the user
        if text_to_analyze:
            result = self.sentiment_analyzer(text_to_analyze)  # Use of sentiment analysis models： Chinese to English
            sentiment = result[0]['label']
            self.display_result(sentiment)
        else:
            self.result_label.config(text="Error: Please enter text to analyze")

    def display_result(self, sentiment):
        self.result_label.config(text=f"Sentiment: {sentiment}")

    def back_to_homepage(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    app = Homepage()
    app.mainloop()
