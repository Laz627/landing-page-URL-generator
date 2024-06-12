import streamlit as st

# Function to generate the campaign URL
def generate_url(root_url, campaign_type, page_type, product, url_slug, offer_variant):
    # Create the URL parts based on provided inputs
    url_parts = [root_url]
    
    if campaign_type:
        url_parts.append(campaign_type)
    if page_type:
        url_parts.append(page_type)
    if product:
        url_parts.append(product)
    if url_slug:
        url_parts.append(url_slug)
    if offer_variant:
        url_parts.append(f"{offer_variant}.html")
    else:
        url_parts.append("")
    
    # Join the parts to form the final URL
    return "/".join(url_parts).rstrip('/')

# Streamlit app
st.title("Campaign URL Generator")

# Input fields with descriptors
root_url = st.text_input("Root Domain", value="https://www.example.com", help="The root domain for the URL, e.g., 'https://www.example.com'")
campaign_type = st.text_input("Campaign Type", value="splash", help="The type of campaign, e.g., 'splash', 'affiliate', 'promotion', etc.")
page_type = st.text_input("Page Type", value="savings-trigger", help="The type of page, e.g., 'savings-trigger', 'rps-trigger', 'checking-trigger', 'landing-page', etc.")
product = st.text_input("Product", value="business-checking", help="The specific product, e.g., 'business-checking', 'business-savings', 'business-credit-cards', etc.")
url_slug = st.text_input("URL Slug Descriptor", value="online-banking-offer", help="A descriptor for the URL slug, e.g., 'online-banking-offer', 'special-deal', 'business-banking-promo', etc.")
offer_variant = st.text_input("Offer Variant", value="a", help="The offer variant, e.g., 'a', 'b', 'c', etc. Leave blank if not applicable.")

# Generate URL button
if st.button("Generate URL"):
    campaign_url = generate_url(root_url, campaign_type, page_type, product, url_slug, offer_variant)
    st.success(f"Generated URL: {campaign_url}")
