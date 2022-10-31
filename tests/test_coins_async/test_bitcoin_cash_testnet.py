from cryptos import coins_async
from cryptos.testing.testcases_async import BaseAsyncCoinTestCase
from cryptos.types import ElectrumXTx, TxOut
from cryptos.electrumx_client.types import ElectrumXMultiBalanceResponse
from typing import List, Type


class TestBitcoinCashTestnet(BaseAsyncCoinTestCase):
    name = "Bitcoin Cash Testnet"
    coin: Type[coins_async.BaseCoin] = coins_async.BitcoinCash
    addresses: List[str] = ["n2DQVQZiA2tVBDu4fNAjKVBS2RArWhfncv",
                            "mnjBtsvoSo6dMvMaeyfaCCRV4hAF8WA2cu",
                            "mmbKDFPjBatJmZ6pWTW6yqXSC6826YLBX6"]
    cash_addresses = ["bchtest:qr3sjptscfm7kqry6s67skm5dgsudwkmcsd7lhzflx",
                      "bchtest:qp83jwvlc8clct6vpskr8jhyayr8u7ynhqd4xj2gld",
                      "bchtest:qpp28cg6sze9la3myp6v28ghg5fjhn9m5yh0kd7ta6"]
    privkeys: List[str] = [
        "098ddf01ebb71ead01fc52cb4ad1f5cafffb5f2d052dd233b3cad18e255e1db1",
        "0861e1bb62504f5e9f03b59308005a6f2c12c34df108c6f7c52e5e712a08e91401",
        "c396c62dfdc529645b822dc4eaa7b9ddc97dd8424de09ca19decce61e6732f71"]  # Private keys for above address_derivations in same order
    privkey_standard_wifs: List[str] = ['91f8DFTsmhtawuLjR8CiHNkgZGPkUqfJ45LxmENPf3k6fuX1m4N',
                                       'cMrziExc6iMV8vvAML8QX9hGDP8zNhcsKbdS9BqrRa1b4mhKvK6f',
                                       "9354Dkk67pJCfmRfMedJPhGPfZCXv2uWd9ZoVNMUtDxjUBbCVZK"]
    multisig_addresses: List[str] = ["", ""]
    fee: int = 500
    max_fee: int = 3500
    testnet: bool = True

    min_latest_height: int = 1524427
    unspent_addresses: List[str] = ["ms31HApa3jvv3crqvZ3sJj7tC5TCs61GSA"]
    unspent: List[ElectrumXTx] = [{'address': 'ms31HApa3jvv3crqvZ3sJj7tC5TCs61GSA',
                                   'height': 1196454,
                                   'tx_hash': '80700e6d1125deafa22b307f6c7c99e75771f9fc05517fc795a1344eca7c8472',
                                   'tx_pos': 0,
                                   'value': 550000000}]
    unspents: List[ElectrumXTx] = unspent
    balance: ElectrumXMultiBalanceResponse = {'confirmed': 550000000, 'unconfirmed': 0}
    balances: List[ElectrumXMultiBalanceResponse] = [{'address': unspent_addresses[0]} | dict(balance)]
    history: List[ElectrumXTx] = [{'height': 1196454, 'tx_hash': '80700e6d1125deafa22b307f6c7c99e75771f9fc05517fc795a1344eca7c8472'}]
    histories: List[ElectrumXTx] = [{'address': unspent_addresses[0]} | dict(history[0])]
    txid: str = "b4dd5908cca851d861b9d2ca267a901bb6f581f2bb096fbf42a28cc2d98e866a"
    txheight: int = 1196454
    block_hash: str = "000000002bab447cbd0c60829a80051e320aa6308d578db3369eb85b2ebb9f46"
    txinputs: List[TxOut] = [{'output': "cbd43131ee11bc9e05f36f55088ede26ab5fb160cc3ff11785ce9cc653aa414b:1", 'value': 96190578808}]
    raw_tx: str = "01000000014b41aa53c69cce8517f13fcc60b15fab26de8e08556ff3059ebc11ee3131d4cb010000006b483045022100b9050a1d58f36a771c4e0869900fb0474b809b134fdad566742e5b3a0ed7580d022065b80e9cc2bc9b921a9b0aad12228d9967345959b021214dbe60b3ffa44dbf0e412102ae83c12f8e2a686fb6ebb25a9ebe39fcd71d981cc6c172fedcdd042536a328f2ffffffff0200ab9041000000001976a914c384950342cb6f8df55175b48586838b03130fad88acd88ed523160000001976a9143479daa7de5c6d8dad24535e648861d4e7e3f7e688ac00000000"


    def test_address_conversion(self):
        for addr, cashaddr in zip(self.addresses, self.cash_addresses):
            convert_cashaddr = self._coin.legacy_addr_to_cash_address(addr)
            self.assertEqual(convert_cashaddr, cashaddr)
            convert_addr = self._coin.cash_address_to_legacy_addr(cashaddr)
            self.assertEqual(addr, convert_addr)

    def test_standard_wif_ok(self):
        self.assertStandardWifOK()
        for privkey, addr in zip(self.privkeys, self.cash_addresses):
            cash_addr = self._coin.privtocashaddress(privkey)
            self.assertEqual(cash_addr, addr)

    async def test_balance(self):
        await self.assertBalanceOK()

    async def test_balances(self):
        await self.assertBalancesOK()

    async def test_unspent(self):
        await self.assertUnspentOK()

    async def test_unspents(self):
        await self.assertUnspentsOK()

    async def test_merkle_proof(self):
        await self.assertMerkleProofOK()

    async def test_history(self):
        await self.assertHistoryOK()

    async def test_histories(self):
        await self.assertHistoriesOK()

    async def test_block_header(self):
        await self.assertBlockHeaderOK()

    async def test_block_headers(self):
        await self.assertBlockHeadersOK()

    async def test_gettx(self):
        await self.assertGetTXOK()

    async def test_getverbosetx(self):
        await self.assertGetVerboseTXOK()

    async def test_gettxs(self):
        await self.assertGetTxsOK()

    async def test_balance_merkle_proven(self):
        await self.assertBalanceMerkleProvenOK()

    async def test_balances_merkle_proven(self):
        await self.assertBalancesMerkleProvenOK()

    async def test_transaction(self):
        """
        Sample transaction:
        TxID:
        """
        await self.assertTransactionOK()

    async def test_transaction_multisig(self):
        """
        Sample transaction:
        TxID:
        """
        await self.assertMultiSigTransactionOK()

    async def test_sendmulti_recipient_tx(self):
        """
        Sample transaction:
        TxID:         """
        await self.assertSendMultiRecipientsTXOK()

    async def test_send(self):
        """
        Sample transaction:
        TxID:
        """
        await self.assertSendOK()

    async def test_subscribe_block_headers(self):
        await self.assertSubscribeBlockHeadersOK()

    async def test_subscribe_block_headers_sync(self):
        await self.assertSubscribeBlockHeadersSyncCallbackOK()

    async def test_latest_block(self):
        await self.assertLatestBlockOK()

    async def test_confirmations(self):
        await self.assertConfirmationsOK()

    async def test_subscribe_address(self):
        await self.assertSubscribeAddressOK()

    async def test_subscribe_address_sync(self):
        await self.assertSubscribeAddressSyncCallbackOK()

    async def test_subscribe_address_transactions(self):
        await self.assertSubscribeAddressTransactionsOK()

    async def test_subscribe_address_transactions_sync(self):
        await self.assertSubscribeAddressTransactionsSyncOK()
