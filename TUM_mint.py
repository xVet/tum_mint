from xrpl.asyncio.clients import AsyncWebsocketClient

from xrpl.transaction import safe_sign_and_submit_transaction,  submit_transaction
from xrpl.models.transactions import NFTokenMint, NFTokenCreateOffer, NFTokenAcceptOffer
#from xrpl.utils import str_to_hex, hex_to_str


import xrpl.wallet

from xrpl.utils.str_conversions import str_to_hex, hex_to_str
import asyncio
import nest_asyncio
nest_asyncio.apply()








content = "HELLO"





async def mint(ipfs):

    hex_ipfs = str_to_hex(f"{ipfs}")

    async with AsyncWebsocketClient("wss://s.altnet.rippletest.net:51233") as client:
        ## create address and fund from faucet
        new_wallet = xrpl.wallet.generate_faucet_wallet(client, debug=True)
        
        print("generated address and funded successful")


        ## create mint nft transaction
        trx = NFTokenMint(
                account=new_wallet.classic_address,
                nftoken_taxon=1,
                transfer_fee = 5000,
                uri = f"{hex_ipfs}",
                flags = 0x00000008 
                )
        

        ## sign the transaction and submit
        submit = safe_sign_and_submit_transaction(trx,new_wallet,client)
        
        print(submit.result)




def main():
    asyncio.run(mint(content))

if __name__ == "__main__":
    main()