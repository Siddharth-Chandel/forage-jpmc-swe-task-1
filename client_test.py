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
      self.assertEqual(data[3], (quote["top_ask"]["price"]+quote["top_bid"]["price"])/2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      isBid = quote["top_bid"]["price"] if quote["top_ask"]["price"]<quote["top_bid"]["price"] else None
      price = (quote["top_bid"]["price"]+quote["top_ask"]["price"])/2
      isPrice = price if quote["top_ask"]["price"]<price else None
      data = getDataPoint(quote)
      self.assertIsNotNone(data)
      bid = data[1] if getRatio(data[1],data[2])>1 else None
      price = data[3] if getRatio(data[3],data[2])>1 else None
      self.assertEqual(isBid, bid)
      self.assertEqual(isPrice, price)


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAGreaterThanEqualToPriceB(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in range(len(quotes)-1):
      price_A = (quotes[quote]["top_bid"]["price"]+quotes[quote]["top_ask"]["price"])/2
      price_B = (quotes[quote+1]["top_bid"]["price"]+quotes[quote+1]["top_ask"]["price"])/2
      greater_1 = price_A if price_A>price_B else price_B
      dataA = getDataPoint(quotes[quote])
      priceA = dataA[3]
      dataB = getDataPoint(quotes[quote+1])
      priceB = dataB[3]
      greater_2 = priceA if getRatio(priceA, priceB)>1 else priceB
      self.assertEqual(greater_1, greater_2)




if __name__ == '__main__':
    unittest.main()
