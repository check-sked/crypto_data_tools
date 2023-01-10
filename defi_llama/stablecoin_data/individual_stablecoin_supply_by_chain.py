import requests
import csv
import datetime

url = "https://stablecoins.llama.fi/stablecoin/1"
response = requests.get(url)
data = response.json()

if "chainBalances" in data:
    print("data written to stablecoin_supply_by_chain.csv")
    with open('stablecoin_supply_by_chain.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Chain", "Date", "Circulating", "Minted"])
        for chain_name, chain_data in data["chainBalances"].items():
            for date_data in chain_data["tokens"]:
                date = datetime.datetime.fromtimestamp(date_data["date"]).strftime("%Y-%m-%d %H:%M:%S")
                circulating = date_data["circulating"]["peggedUSD"]
                minted = date_data["minted"]["peggedUSD"]

                writer.writerow([chain_name, date, circulating, minted])
else:
    print("ChainBalances field not found in the JSON response")

