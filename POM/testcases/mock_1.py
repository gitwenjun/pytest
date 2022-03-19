
import pytest

from TestCases.mock import Product
def test_p(mocker):
    product = Product()
    mock_values = {"id":1,"name":"苹果","num":23}
    product.get_product_status_by_id = mocker.patch("TestCases.mock.Product.get_product_status_by_id",return_value=mock_values)
    r = product.buy_product(1)
    print(r)
    assert r.get('status') == 0

if __name__ == '__main__':
    pytest.main(['-sv','mock_1.py'])