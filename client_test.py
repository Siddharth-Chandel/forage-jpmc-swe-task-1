import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      data = getDataPoint(quote)
      self.assertIsNotNone(data)
      print(f"Stock: {data[0]}, Price: {data[3]}")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      data = getDataPoint(quote)
      self.assertIsNotNone(data)
      stock, bid, ask, price = data
      print(f"Stock: {stock}")
      self.assertGreater(bid, ask)
      self.assertGreater(price, ask)
      print("Bid and price is greater than ask")


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAGreaterThanEqualToPriceB(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in range(len(quotes)-1):
      dataA = getDataPoint(quotes[quote])
      stockA, priceA = dataA[0], dataA[3]
      dataB = getDataPoint(quotes[quote+1])
      stockB, priceB = dataB[0], dataB[3]
      self.assertGreaterEqual(getRatio(priceA, priceB),1)
      print(f"{stockA}'s price is greater than and equal to {stockB}'s price")




if __name__ == '__main__':
    unittest.main()
