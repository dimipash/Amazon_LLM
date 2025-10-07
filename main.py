import streamlit as st
from src.oxylabs_client import scrape_product_details

def render_header():
    st.title("Amazon Competitor Analysis")
    st.caption("Enter your ASIN to get product insights")

def render_inputs():
    asin = st.text_input("ASIN", placeholder="e.g., BOXVBA224466")
    geo = st.text_input("Zip/Postal Code", placeholder="e.g., 8000")
    domain = st.selectbox("Domain", [
        "com", "co.uk", "de", "fr", "it", "es", "ae"
    ])
    return asin.strip(), geo.strip(), domain

def main():
    st.set_page_config(page_title="Amazon Competitor Analysis", page_icon=":robot:")
    render_header()
    asin, geo, domain = render_inputs()

    if st.button("Scrape product") and asin:
        with st.spinner("Scraping product..."):
            st.write("Scrape")
            product = scrape_product_details(asin, geo, domain)
        st.success("Product scraped successfully!")
        st.write(product)


if __name__ == "__main__":
    main()