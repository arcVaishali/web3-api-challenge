import requests
account_address = "0xD983d04960D619C0E10DB52B12B75cC8c54CD58D"
url = f"https://deep-index.moralis.io/api/v2.2/wallets/{account_address}/chains"
headers = {
    "accept": "application/json",
    "X-API-Key": "MORALIS_API_KEY",
}
params = {"chains[0]": "eth", "chains[1]": "polygon"}

response = requests.get(url, headers=headers, params=params)

print(response.json())


# # Define the URL you want to send the GET request to
# url = 'https://deep-index.moralis.io/api/v2.2/wallets/0xD983d04960D619C0E10DB52B12B75cC8c54CD58D/chains'

# # Send the GET request
# response = requests.get(url)

# # Check if the request was successful (HTTP status code 200)
# if response.status_code == 200:
#     # Print the response content (usually in JSON format)
#     print(response.json())
# else:
#     # Handle the error
#     print(f"HTTP Request failed with status code: {response.status_code}")

# api_key = "atKFB00XlOajHYj1jjsGjPg9Ht75t5dFa43SoznLBubtkqMOlHxZnWQP6D2EVwJx"

# params = {
#     "address": "0xD983d04960D619C0E10DB52B12B75cC8c54CD58D",
#     "chains": ["eth", "bsc", "polygon"],
# }

# result = evm_api.transaction.get_wallet_active_chains(
#     api_key=api_key,
#     params=params,
# )

# print(result)