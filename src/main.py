from moltin.moltin import Moltin
import pprint 

m = Moltin('CKVntdOscTXDWG216d0g4j9VEs15D4sIrXB7zbLnc8', 'j5MDDb3eyqThYwfwUNcYF1vv8ivKXh2xcBobPk5uqd')
access_token = m.authenticate()

product = m.Product.find_by({"slug": "for-my-love-on-our-anniversary"})

pprint.pprint(product)