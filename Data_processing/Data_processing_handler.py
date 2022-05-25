import Scarping_module
import Filter_sentences_module


# main function
if __name__ == '__main__':
    df_scraped = Scarping_module.scrape_thinkil()
    df_filtered = Filter_sentences_module.filter_sentences_with_numbers(df_scraped["text"])



