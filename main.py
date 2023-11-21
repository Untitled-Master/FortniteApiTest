import requests

def get_fortnite_shop_data():
    # API endpoint URL
    api_url = "https://fortnite-api.com/v2/shop/br"

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the expected data is present in the response
            if 'data' in data and 'featured' in data['data'] and 'entries' in data['data']['featured']:
                featured_items = data['data']['featured']['entries']

                # Loop through featured items and print organized information
                for item in featured_items:
                    item_name = item['items'][0]['name']
                    item_description = item['items'][0]['description']
                    item_price = item['finalPrice']
                    item_rarity = item['items'][0]['rarity']['displayValue']
                    item_introduction = item['items'][0]['introduction']['text']

                    # Organize information without asterisks
                    formatted_info = f"✨ {item_name}\n\n" \
                                     f"📄 𝑫𝒆𝒔𝒄𝒓𝒊𝒑𝒕𝒊𝒐𝒏: {item_description}\n" \
                                     f"💰 𝑷𝒓𝒊𝒄𝒆: {item_price}\n" \
                                     f"🌟 𝑹𝒂𝒓𝒊𝒕𝒚: {item_rarity}\n" \
                                     f"📖 𝑰𝒏𝒕𝒓𝒐𝒅𝒖𝒄𝒕𝒊𝒐𝒏: {item_introduction}\n" \
                                     "---------------------------------------"

                    # Print the formatted information
                    print(formatted_info)

            else:
                print("Error: Unexpected data structure in the API response.")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get Fortnite shop data
get_fortnite_shop_data()
